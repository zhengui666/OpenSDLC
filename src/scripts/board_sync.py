"""Optional, dependency-free board event planner; no network or credential access."""
import argparse
import hashlib
import json
import re
from pathlib import Path

FIELDS = {"title", "status", "detail", "next", "evidence"}
STATUSES = {"pending", "in_progress", "blocked", "paused", "done"}
ID = re.compile(r"[A-Za-z0-9_-]{1,100}\Z")


class Conflict(Exception):
    """An adapter must translate a board 409 into this exception."""


def stable_id(project_id, source_id):
    """Persist project_id; source_id is the original task ID, never its title."""
    if not isinstance(project_id, str) or not ID.fullmatch(project_id):
        raise ValueError("Invalid project ID")
    if not isinstance(source_id, str) or not source_id:
        raise ValueError("A stable source ID is required")
    raw = json.dumps([project_id, source_id], ensure_ascii=False).encode("utf-8")
    return "osdlc_" + hashlib.sha256(raw).hexdigest()


def validate_event(event):
    if not isinstance(event, dict) or set(event) - {"id", "parentId", "patch"}:
        raise ValueError("Event accepts only id, parentId and patch")
    if not isinstance(event.get("id"), str) or not ID.fullmatch(event["id"]):
        raise ValueError("Invalid event ID")
    parent = event.get("parentId")
    if parent is not None and (not isinstance(parent, str) or not ID.fullmatch(parent)):
        raise ValueError("Invalid parent ID")
    if parent == event["id"]:
        raise ValueError("A task cannot parent itself")
    patch = event.get("patch")
    if not isinstance(patch, dict) or not patch or set(patch) - FIELDS:
        raise ValueError("Invalid patch fields")
    for key, value in patch.items():
        if not isinstance(value, str) or len(value) > (160 if key == "title" else 5000):
            raise ValueError("Invalid patch value")
        if key == "title" and not value.strip():
            raise ValueError("Title cannot be empty")
        if key == "status" and value not in STATUSES:
            raise ValueError("Invalid status")


def plan(snapshot, event):
    """Return a CAS request or a reason to skip; never delete, unlock or restore."""
    validate_event(event)
    revision = snapshot["revision"]
    if type(revision) is not int or revision < 0:
        raise ValueError("Invalid revision")
    rows = snapshot["board"]["tasks"]
    records = {row["id"]: row for row in rows}
    if len(records) != len(rows):
        raise ValueError("Duplicate board IDs")
    current = records.get(event["id"])
    if current and current.get("deletedAt"):
        return {"outcome": "deleted", "request": None}
    # Validate the complete ancestor chain, including deletions and cycles.
    parent = event.get("parentId", current.get("parentId") if current else None)
    seen = {event["id"]}
    ancestor = parent
    while ancestor is not None:
        if ancestor in seen:
            return {"outcome": "invalid_parent", "request": None}
        seen.add(ancestor)
        row = records.get(ancestor)
        if not row or row.get("deletedAt"):
            return {"outcome": "unavailable_parent", "request": None}
        ancestor = row.get("parentId")
    # Moving an existing node needs a separate user decision, not a status event.
    if current and "parentId" in event and current.get("parentId") != parent:
        return {"outcome": "parent_mismatch", "request": None}
    locks = set(current.get("locks", [])) if current else set()
    patch = {key: value for key, value in event["patch"].items()
             if key not in locks and (not current or current.get(key) != value)}
    skipped = sorted(key for key in event["patch"] if key in locks
                     and current.get(key) != event["patch"][key])
    if not current and (not patch.get("title") or "status" not in patch):
        raise ValueError("Creating a task requires title and status")
    if not patch:
        return {"outcome": "locked" if skipped else "unchanged",
                "skipped": skipped, "request": None}
    operation = {"action": "update" if current else "create", "id": event["id"], "patch": patch}
    if not current:
        operation["parentId"] = parent
    return {"outcome": "planned", "skipped": skipped,
            "request": {"revision": revision, "operation": operation}}


def synchronize(read, update, event, max_conflicts=3):
    """Use injected existing host adapters. Refresh and replan only revision conflicts.

    Transport errors propagate: the caller must reconcile uncertain writes before
    retrying. Return metadata only, never a false claim that blocked fields synced.
    """
    snapshot = read()
    conflicts = 0
    while True:
        result = plan(snapshot, event)
        if result["request"] is None:
            return result
        try:
            response = update(result["request"])
        except Conflict:
            fresh = read()
            replanned = plan(fresh, event)
            if replanned["request"] is None:
                return replanned
            if fresh["revision"] == snapshot["revision"]:
                return {"outcome": "rejected", "request": None}
            conflicts += 1
            if conflicts >= max_conflicts:
                return {"outcome": "conflict", "request": None}
            snapshot = fresh
            continue
        # The API returns the updated board. Confirm its values, not just HTTP 200.
        verified = plan(response, event)
        if (response["revision"] <= snapshot["revision"]
                or verified["outcome"] not in {"unchanged", "locked"}):
            return {"outcome": "unverified", "request": None}
        skipped = sorted(set(result["skipped"]) | set(verified.get("skipped", [])))
        return {"outcome": "partial" if skipped else "synced",
                "skipped": skipped, "revision": response["revision"], "request": None}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    identity = commands.add_parser("id")
    identity.add_argument("project_id")
    identity.add_argument("source_id")
    planner = commands.add_parser("plan")
    planner.add_argument("snapshot", type=Path)
    planner.add_argument("event", type=Path)
    args = parser.parse_args()
    if args.command == "id":
        print(stable_id(args.project_id, args.source_id))
    else:
        print(json.dumps(plan(json.loads(args.snapshot.read_text()),
                              json.loads(args.event.read_text())), ensure_ascii=False))


if __name__ == "__main__":
    main()
