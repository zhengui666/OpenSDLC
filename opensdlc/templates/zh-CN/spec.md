<!-- 落点: .opensdlc/tasks/<task-id>/spec.md
复用已有任务标识。新任务须先读 .opensdlc/config.json：zh-CN 必须用简体中文名（修复登录超时）；en、未配置或回退英文时必须用英文名（fix-login-timeout）。目录名、task_id 与引用须一致，不随语言切换重命名。
从 task.md#spec 链接。仅展开受影响的方面，但必须明确正常与失败行为。调研和设计决策放在此处，不另建台账。
用事实替换占位符。可删除不需展开的提示，不得删掉必要行为。模板不证明工作已经执行。 -->

# {{task_title}} — 需求与设计

<a id="basis"></a>
## 意图与约束

**被接受的意图与适用权威规则：** {{basis}}

**范围与非目标：** {{scope}}

<a id="acceptance"></a>
## 行为与验收

| 场景 | 可观察的预期结果 | 验证方式 |
| --- | --- | --- |
| {{scenario}} | {{expected_result}} | {{verification_method}} |

<a id="design"></a>
## 设计

**现有流程、复用与目标变化：** {{flow}}

**接口、输入输出与数据契约：** {{contracts}}

**权限、隐私与信任边界：** {{permissions}}

**UX、可访问性与认可的视觉参考：** {{ux}}

**失败、并发、兼容及迁移行为：** {{failure_behavior}}

<a id="decisions"></a>
## 取舍与决定

**已核实的调研与依据：** {{research}}

**替代方案与选定方案：** {{alternatives}}

**冲突、责任人与解决方式：** {{conflicts}}

**需求接受、技术咨询与进入构建的决定：** {{acceptance_decision}}
