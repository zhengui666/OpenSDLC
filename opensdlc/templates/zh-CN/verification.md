<!-- 落点: .opensdlc/tasks/<task-id>/verification.md
复用已有任务标识。新任务须先读 .opensdlc/config.json：zh-CN 必须用简体中文名（修复登录超时）；en、未配置或回退英文时必须用英文名（fix-login-timeout）。目录名、task_id 与引用须一致，不随语言切换重命名。
从 task.md#verification 链接。记录实际观察，不写期望结果。零测试、排队、超时与未运行均非通过；链接完整报告，不复制日志。
用事实替换占位符。可删除不需展开的提示，不得删掉必要行为。模板不证明工作已经执行。 -->

# {{task_title}} — 验证

<a id="scope"></a>
## 已检查的实现

**提交／分支／相关未提交修改或原生构建引用：** {{implementation}}

**环境、配置与时间／运行标识：** {{environment}}

**覆盖的验收：** {{acceptance}}

<a id="checks"></a>
## 实际检查

| 命令或直接检查 | 结果与相关输出 | 报告／依据 |
| --- | --- | --- |
| {{check}} | {{actual_result}} | {{evidence}} |

<a id="regression"></a>
## 回归与行为

**修复前缺陷复现及预期失败原因：** {{before_fix}}

**修复后行为及相邻调用方／流程：** {{after_fix}}

**真实 UI 观察与认可参考的比较：** {{visual_checks}}

**修改测试预期的理由与审查：** {{test_changes}}

<a id="independent"></a>
## 独立验收

**必要时的验证者、独立上下文、范围与实际结果：** {{independent_result}}

<a id="gaps"></a>
## 剩余缺口

**既有失败与新增回归：** {{failures}}

**未运行检查、限制与下一步：** {{gaps}}
