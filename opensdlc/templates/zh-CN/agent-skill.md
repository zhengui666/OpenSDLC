---
name: "{{skill_name}}"
description: "{{trigger_description}}"
---

<!-- 落点: <active-native-skill-directory>/<skill-name>/SKILL.md（当前启用的原生 Skill 目录）
仅为真实重复知识或行为创建。替换全部占位符，Skill 名称与所在目录一致，并验证应触发与不应触发的实例。不将此模板复制成第二个 OpenSDLC 入口。
用事实替换占位符。可删除不需展开的提示，不得删掉必要行为。模板不证明工作已经执行。 -->

# {{skill_title}}

<a id="scope"></a>
## 范围与依据

**目标、非目标与规则负责人：** {{purpose}}

**权威输入与规则：** {{sources}}

<a id="inputs"></a>
## 所需上下文

**执行前需读取与核实的内容：** {{inputs}}

<a id="procedure"></a>
## 执行步骤

1. {{read_and_understand}}
2. {{reuse_and_execute}}
3. {{verify_and_report}}

<a id="outputs"></a>
## 输出

**预期结果、权威落点与最小适用模板：** {{outputs}}

<a id="language"></a>
## 文档语言

读取仓库 `.opensdlc/config.json`：文件或 `language` 缺失时默认 `en`，`zh-CN` 选择简体中文。新正文和新任务标识必须使用解析后的语言：中文如 `修复登录超时`，英文如 `fix-login-timeout`。原样复用已有任务标识；固定文件名、锚点与代码标识符不变。除非要求翻译，否则保留已有文档语言。

<a id="boundaries"></a>
## 边界与失败处理

**权限、非目标与前置条件缺失时的处理：** {{boundaries}}

<a id="checks"></a>
## 触发与行为检查

**必须触发与不能触发的真实请求：** {{trigger_examples}}

**可运行／可观察行为检查与认可结果：** {{checks}}
