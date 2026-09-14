<!-- 落点: .opensdlc/tasks/<task-id>/handoff.md
复用已有任务标识。新任务须先读 .opensdlc/config.json：zh-CN 必须用简体中文名（修复登录超时）；en、未配置或回退英文时必须用英文名（fix-login-timeout）。目录名、task_id 与引用须一致，不随语言切换重命名。
从 task.md#handoff 链接。保留当前恢复入口，不记录逐轮对话。接手 Agent 必须核实真实工作区与远端状态后再继续。
用事实替换占位符。可删除不需展开的提示，不得删掉必要行为。模板不证明工作已经执行。 -->

# {{task_title}} — 交接

<a id="goal"></a>
## 目标与决定

**任务入口与约定终点：** {{task_and_endpoint}}

**已接受决定与重要约束：** {{decisions}}

<a id="workspace"></a>
## 工作区

**仓库／工作树／分支及相关修改：** {{workspace}}

**需保留的其他修改：** {{preserve}}

<a id="progress"></a>
## 实际进展

**已完成工作与验证引用：** {{completed}}

**剩余工作、阻塞与负责人：** {{remaining}}

<a id="external"></a>
## 外部状态

**待复核的 PR／CI／审查／部署状态：** {{remote_state}}

**超时或不确定写入；重试前先查询：** {{uncertain_actions}}

<a id="resume"></a>
## 恢复

**首个下一步及具体命令／工作目录：** {{resume_steps}}

**所需访问与申请入口：** {{access}}
