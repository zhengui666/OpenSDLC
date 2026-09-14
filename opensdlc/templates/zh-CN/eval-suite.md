<!-- 落点: .opensdlc/evals/suite.md
评估 Agent 完成任务的能力，而不只是产品单测。复用真实任务、已有运行器与权威报告。不编造样例数量或基线。
用事实替换占位符。可删除不需展开的提示，不得删掉必要行为。模板不证明工作已经执行。 -->

# Agent 评测集

<a id="scope"></a>
## 目标与责任

**Agent 工作流与负责人：** {{workflow_and_owner}}

**相关模型、指令、Skills、Hooks 与工具配置位置：** {{configuration}}

<a id="cases"></a>
## 代表样例

| 样例／数据集位置 | 真实来源 | 覆盖行为／规则 |
| --- | --- | --- |
| {{case_location}} | {{real_source}} | {{coverage}} |

<a id="execution"></a>
## 执行

**具体非交互命令、工作目录与环境：** {{command}}

**所需访问、隔离、预算与限制：** {{requirements}}

**配置变更触发与定时／约定离线周期：** {{triggers}}

<a id="comparison"></a>
## 验收与比较

**可接受结果与可运行检查：** {{acceptance}}

**认可基线及其实际配置／报告：** {{baseline}}

**配置发布前的退化审查与决定：** {{regression_review}}

<a id="maintenance"></a>
## 维护

**生产事故转永久回归样例：** {{incident_cases}}

**更新陈旧样例与报告限制：** {{maintenance}}
