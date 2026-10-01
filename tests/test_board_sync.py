import copy
import importlib.util
from pathlib import Path
import unittest

MODULE = Path(__file__).resolve().parents[1] / "src/scripts/board_sync.py"
spec = importlib.util.spec_from_file_location("board_sync", MODULE)
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)


class Board:
    """In-memory contract server: every request checks CAS, locks and tombstones."""
    def __init__(self):
        self.snapshot = {"revision": 0, "board": {"tasks": [], "events": []}}
        self.requests = []
        self.before_update = None

    def read(self):
        return copy.deepcopy(self.snapshot)

    def update(self, request):
        self.requests.append(copy.deepcopy(request))
        if self.before_update:
            callback, self.before_update = self.before_update, None
            callback()
        if request["revision"] != self.snapshot["revision"]:
            raise sync.Conflict()
        op = request["operation"]
        rows = self.snapshot["board"]["tasks"]
        row = next((r for r in rows if r["id"] == op["id"]), None)
        if row and (row.get("deletedAt") or set(op["patch"]) & set(row["locks"])):
            raise sync.Conflict()
        if op["action"] == "create":
            if row:
                raise sync.Conflict()
            parent = op.get("parentId")
            if parent and not any(r["id"] == parent and not r["deletedAt"] for r in rows):
                raise sync.Conflict()
            row = {"id": op["id"], "parentId": parent, "locks": [], "deletedAt": None}
            rows.append(row)
        elif op["action"] != "update" or row is None:
            raise sync.Conflict()
        row.update(op["patch"])
        self.snapshot["revision"] += 1
        return self.read()

    def send(self, identity, parent=None, **patch):
        return sync.synchronize(self.read, self.update,
                                {"id": identity, "parentId": parent, "patch": patch})


class Tests(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.board.send("project", title="Example", status="in_progress")

    def test_workflow_event_replay(self):
        b = self.board
        task = sync.stable_id("project", "fix-timeout")
        child = sync.stable_id("project", "write-regression")
        leaf = sync.stable_id("project", "check-retry")
        for identity, parent, title in [(task, "project", "Fix timeout"),
                                         (child, task, "Regression"), (leaf, child, "Retry")]:
            self.assertEqual(b.send(identity, parent, title=title, status="pending")["outcome"], "synced")
        for stage, status in [("Plan", "in_progress"), ("Design", "in_progress"),
                              ("Build", "blocked"), ("Build", "paused"),
                              ("Build", "in_progress"), ("Test", "in_progress"),
                              ("Deliver", "done")]:
            event = {"id": task, "parentId": "project", "patch": {"status": status, "detail": "Stage: " + stage}}
            self.assertEqual(sync.synchronize(b.read, b.update, event)["outcome"], "synced")
            revision = b.snapshot["revision"]
            self.assertEqual(sync.synchronize(b.read, b.update, event)["outcome"], "unchanged")
            self.assertEqual(revision, b.snapshot["revision"])
        self.assertEqual(b.send(task, "project", title="Renamed title")["outcome"], "synced")
        self.assertEqual(len(b.snapshot["board"]["tasks"]), 4)
        self.assertEqual(b.requests[-1]["operation"]["patch"], {"title": "Renamed title"})

    def test_stable_unicode_identity(self):
        self.assertEqual(sync.stable_id("project", "修复超时"), sync.stable_id("project", "修复超时"))
        self.assertNotEqual(sync.stable_id("project", "task"), sync.stable_id("other", "task"))
        self.assertTrue(sync.ID.fullmatch(sync.stable_id("project", "修复超时")))

    def test_locks_partial_and_tombstone(self):
        b = self.board
        row = b.snapshot["board"]["tasks"][0]
        row["locks"] = ["title"]
        result = b.send("project", title="Auto rename", status="blocked")
        self.assertEqual(result["outcome"], "partial")
        self.assertEqual(row["title"], "Example")
        self.assertEqual(b.send("project", title="Auto rename")["outcome"], "locked")
        row["deletedAt"] = "2026-01-01T00:00:00Z"
        count = len(b.requests)
        self.assertEqual(b.send("project", title="Revive")["outcome"], "deleted")
        self.assertEqual(b.send("child", "project", title="Child", status="pending")["outcome"], "unavailable_parent")
        self.assertEqual(count, len(b.requests))

    def test_conflict_replans_user_lock(self):
        b = self.board
        def mutate():
            row = b.snapshot["board"]["tasks"][0]
            row.update(title="User title", locks=["title"])
            b.snapshot["revision"] += 1
        b.before_update = mutate
        result = b.send("project", title="Auto title", status="blocked")
        self.assertEqual(result["outcome"], "partial")
        self.assertEqual(b.requests[-1]["operation"]["patch"], {"status": "blocked"})
        self.assertEqual(b.snapshot["board"]["tasks"][0]["title"], "User title")

    def test_conflict_tombstone_no_retry(self):
        b = self.board
        def mutate():
            b.snapshot["board"]["tasks"][0]["deletedAt"] = "now"
            b.snapshot["revision"] += 1
        b.before_update = mutate
        count = len(b.requests)
        self.assertEqual(b.send("project", status="done")["outcome"], "deleted")
        self.assertEqual(len(b.requests), count + 1)

    def test_same_revision_rejection_stops(self):
        calls = []
        def reject(request):
            calls.append(request)
            raise sync.Conflict()
        result = sync.synchronize(self.board.read, reject, {"id": "project", "patch": {"status": "done"}})
        self.assertEqual(result["outcome"], "rejected")
        self.assertEqual(len(calls), 1)

    def test_uncertain_error_not_retried(self):
        def timeout(request):
            raise TimeoutError("uncertain write")
        with self.assertRaises(TimeoutError):
            sync.synchronize(self.board.read, timeout, {"id": "project", "patch": {"status": "done"}})

    def test_missing_parent_and_move(self):
        b = self.board
        self.assertEqual(b.send("child", "missing", title="Child", status="pending")["outcome"], "unavailable_parent")
        b.send("child", "project", title="Child", status="pending")
        self.assertEqual(b.send("child", None, status="done")["outcome"], "parent_mismatch")
        self.assertEqual(b.send("project", "child", status="done")["outcome"], "invalid_parent")

    def test_validation_rejects_privileged_fields(self):
        for patch in [{"deletedAt": None}, {"locks": []}, {"status": "completed"}, {"title": "x" * 161}, {"detail": "x" * 5001}]:
            with self.assertRaises(ValueError):
                sync.plan(self.board.read(), {"id": "project", "patch": patch})

    def test_unverified_response(self):
        result = sync.synchronize(self.board.read, lambda _: self.board.read(),
                                  {"id": "project", "patch": {"status": "done"}})
        self.assertEqual(result["outcome"], "unverified")

    def test_bounded_contended_revision(self):
        calls = []
        def reject(request):
            calls.append(request)
            self.board.snapshot["revision"] += 1
            raise sync.Conflict()
        result = sync.synchronize(self.board.read, reject, {"id": "project", "patch": {"status": "done"}})
        self.assertEqual(result["outcome"], "conflict")
        self.assertEqual(len(calls), 3)


if __name__ == "__main__":
    unittest.main()
