<!-- 落点: .opensdlc/tasks/<task-id>/task.md
复用已有任务标识。新任务须先读 .opensdlc/config.json：zh-CN 必须用简体中文名（修复登录超时）；en、未配置或回退英文时必须用英文名（fix-login-timeout）。目录名、task_id 与引用须一致，不随语言切换重命名。
任务默认记录。推进到相应阶段时再添加章节，小任务保持简短。正文已有外部权威来源或已拆分时，该章节只保留链接及必要本地信息。
用事实替换占位符。可删除不需展开的提示，不得删掉必要行为。模板不证明工作已经执行。 -->

# {{task_title}}

<a id="task"></a>
## 任务

**任务标识：** {{task_id}}

**原始请求／工单／事故：** {{source}}

**约定终点及合并／发布范围：** {{endpoint}}

<a id="intent"></a>
## 意图

**问题、受影响用户／系统及预期结果：** {{intent}}

**范围、约束与非目标：** {{scope}}

**开放问题及需求负责人决定／实际引用：** {{intent_decision}}

<a id="spec"></a>
## 需求与设计

**预期行为与可观察的验收结果：** {{acceptance}}

**适用接口、数据、UX、权限、错误及兼容行为：** {{design}}

**冲突、解决方式与进入构建的决定：** {{design_decision}}

<a id="plan"></a>
## 实现计划

**已检查的流程、调用方与复用点：** {{reuse}}

**有序修改、具体路径与验证：** {{steps}}

**风险、替代方案与工程确认：** {{plan_decision}}

<a id="verification"></a>
## 验证

**实际检查的实现与环境：** {{checked_scope}}

**命令／直接观察、实际结果与原生报告链接：** {{checks}}

**适用时的修复前后复现：** {{regression}}

**失败、未运行检查与覆盖缺口：** {{verification_gaps}}

<a id="review"></a>
## 审查

**PR／审查者及审查范围：** {{review_source}}

**发现、修复、复审与当前 CI：** {{review_results}}

**未解决问题及真实人工批准／待决定事项：** {{review_remaining}}

<a id="delivery"></a>
## 交付

**实际 PR／合并／部署入口及核实状态：** {{delivery_result}}

**涉及发布时的发布记录：** {{release_reference}}

**未完成工作与下一步：** {{remaining_work}}

<a id="handoff"></a>
## 交接

**工作树／分支／未提交修改：** {{workspace}}

**关键决定与当前阻塞：** {{handoff_context}}

**重试前需核对的外部动作：** {{external_state}}

**下一步、恢复命令与所需访问：** {{resume}}
