<!-- 落点: .opensdlc/tasks/<task-id>/review.md
复用已有任务标识。新任务须先读 .opensdlc/config.json：zh-CN 必须用简体中文名（修复登录超时）；en、未配置或回退英文时必须用英文名（fix-login-timeout）。目录名、task_id 与引用须一致，不随语言切换重命名。
从 task.md#review 链接。评论、批准与 CI 以 PR 平台为准。作者自审不等于独立审查或人工批准。
用事实替换占位符。可删除不需展开的提示，不得删掉必要行为。模板不证明工作已经执行。 -->

# {{task_title}} — 审查

<a id="scope"></a>
## 审查依据

**PR 与实际候选版本：** {{candidate}}

**审查者／审查类型与适用规则：** {{reviewer}}

**意图、规格与计划引用：** {{basis}}

<a id="findings"></a>
## 发现与处理

| 问题／严重度 | 位置与影响 | 处理／实际复审 |
| --- | --- | --- |
| {{finding}} | {{location_and_impact}} | {{resolution}} |

<a id="outcome"></a>
## 当前结论

**最新检查与复审引用：** {{checks}}

**未解决问题：** {{unresolved}}

**真实人工批准或待决定事项：** {{approval}}

**需纠正的重复问题或陈旧上下文：** {{learning}}
