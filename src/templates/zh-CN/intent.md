<!-- 落点: .opensdlc/tasks/<task-id>/intent.md
复用已有任务标识。新任务须先读 .opensdlc/config.json：zh-CN 必须用简体中文名（修复登录超时）；en、未配置或回退英文时必须用英文名（fix-login-timeout）。目录名、task_id 与引用须一致，不随语言切换重命名。
仅在意图需要独立成文时使用。从 task.md#intent 链接到此处，不在那里保留第二份正文。
用事实替换占位符。可删除不需展开的提示，不得删掉必要行为。模板不证明工作已经执行。 -->

# {{task_title}} — 意图

<a id="source"></a>
## 来源与责任

**原始请求与需求负责人：** {{source_and_owner}}

<a id="problem"></a>
## 问题与预期结果

**发起人表述的问题：** {{problem}}

**受影响用户与系统：** {{affected_parties}}

**预期结果与可观察的成功标准：** {{outcome}}

<a id="scope"></a>
## 范围

**范围内：** {{in_scope}}

**约束：** {{constraints}}

**非目标：** {{non_goals}}

<a id="decision"></a>
## 问题与接受决定

**未知项及解决方式：** {{open_questions}}

**发起人纠正：** {{corrections}}

**已接受／退回／待定及实际决定引用：** {{decision}}
