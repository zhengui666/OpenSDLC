---
name: "{{agent_name}}"
description: "{{trigger_description}}"
tools: "{{native_tool_list}}"
---

<!-- 落点: .claude/agents/<agent-name>.md（其他宿主仅按已核实的原生契约调整）
本 frontmatter 面向 Claude Code。使用宿主支持的名称，仅选择实际需要的工具。其他宿主须使用其已核实的原生配置，不假设本文在那里会启用 Agent。
用事实替换占位符。可删除不需展开的提示，不得删掉必要行为。模板不证明工作已经执行。 -->

# {{agent_title}}

<a id="role"></a>
## 角色与边界

**一项有用的重复职责：** {{responsibility}}

**禁止执行的事项：** {{non_goals}}

<a id="input"></a>
## 任务输入

**已接受计划／工作包、具体输入与范围：** {{input}}

**可操作路径、隔离与工具边界：** {{limits}}

<a id="procedure"></a>
## 执行步骤

1. 读取提供的计划以及实际代码或依据。
2. {{perform_bounded_task}}
3. 使用 {{verification_method}} 验证结果。
4. 将发现与依据返回协调者；不另写一份报告，不并发修改共享记录。

<a id="output"></a>
## 返回格式

**结果、依据、缺口与下一步：** {{return_format}}

**供协调者汇总的父任务落点：** {{parent_destination}}

<a id="verification-role"></a>
## 验证者职责分离

担任验证者时只核验并报告，由作者修复实现。读取仓库 `.opensdlc/config.json` 决定文档语言与新任务命名：`zh-CN` 必须用简体中文任务名，`en`、默认或回退英文时必须用英文。复用已分配的任务标识，不因语言切换重命名。不得凭文字授予权限或声称获得批准。
