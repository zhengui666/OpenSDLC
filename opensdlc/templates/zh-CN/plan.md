<!-- 落点: .opensdlc/tasks/<task-id>/plan.md
复用已有任务标识。新任务须先读 .opensdlc/config.json：zh-CN 必须用简体中文名（修复登录超时）；en、未配置或回退英文时必须用英文名（fix-login-timeout）。目录名、task_id 与引用须一致，不随语言切换重命名。
从 task.md#plan 链接。先只读勘察，不同时修改实现。只纳入满足已接受规格所需的工作。
用事实替换占位符。可删除不需展开的提示，不得删掉必要行为。模板不证明工作已经执行。 -->

# {{task_title}} — 实现计划

<a id="basis"></a>
## 起点

**已接受的意图与规格：** {{basis}}

**已检查文件、端到端流程与共享调用方：** {{investigation}}

**拟复用代码／标准库／原生能力／已有依赖：** {{reuse}}

<a id="steps"></a>
## 执行顺序

| 步骤 | 具体路径与修改 | 依赖 | 验证 |
| --- | --- | --- | --- |
| {{step}} | {{paths_and_change}} | {{dependency}} | {{check}} |

<a id="risks"></a>
## 风险与替代方案

**最可能破坏的行为与最高风险步骤：** {{risks}}

**未采用方案及理由：** {{alternatives}}

**适用时的恢复／回退：** {{recovery}}

<a id="parallel"></a>
## 独立工作包

**仅在有收益时填写：目标、输入、负责人、可写路径、隔离、检查与集成顺序：** {{work_packages}}

<a id="decision"></a>
## 工程确认与偏离

**真实计划接受与重大风险咨询：** {{decision}}

**当前偏离及所需规格决定：** {{deviations}}
