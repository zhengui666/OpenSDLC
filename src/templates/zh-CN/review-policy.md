<!-- 落点: .opensdlc/review.md
跨任务复用。已有权威规则时，在此路径使用 source-link 模板，不重复正文。
用事实替换占位符。可删除不需展开的提示，不得删掉必要行为。模板不证明工作已经执行。 -->

# 项目审查规则

<a id="scope"></a>
## 范围与依据

**代码负责人、技术负责人及权威标准：** {{owners_and_sources}}

**纳入范围与明确排除的生成内容／已有检查覆盖项：** {{scope}}

<a id="focus"></a>
## 审查重点

**正确性、失败处理与回归风险：** {{correctness}}

**安全、隐私与权限：** {{security}}

**意图／规格／计划一致性；复用与设计原则：** {{design}}

**测试差异有效性与文档准确性：** {{tests_and_docs}}

<a id="severity"></a>
## 严重度与响应

| 严重度 | 具体定义 | 所需响应／原生执行位置 |
| --- | --- | --- |
| {{severity}} | {{definition}} | {{response}} |

<a id="approval"></a>
## 审查与批准

**人工审查阈值与实际分支／平台设置：** {{human_threshold}}

**修复、验证及请求复审流程：** {{review_loop}}

<a id="quality"></a>
## 发现质量

**质量负责人、复查周期与降噪措施：** {{quality_review}}

**需补入项目上下文的重复问题：** {{context_feedback}}
