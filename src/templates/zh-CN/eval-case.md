<!-- 落点: .opensdlc/evals/cases/<case-id>.md
仅在已有可执行数据集未承载该样例时使用。区分任务输入与评估者指令；使用脱敏数据。
用事实替换占位符。可删除不需展开的提示，不得删掉必要行为。模板不证明工作已经执行。 -->

# {{case_title}}

<a id="source"></a>
## 来源与目标

**样例标识与真实任务／事故来源：** {{source}}

**本样例能区分的行为或失败：** {{purpose}}

<a id="setup"></a>
## 起始条件

**仓库／测试素材／初始状态：** {{setup}}

**可用工具、环境与约束：** {{environment}}

<a id="input"></a>
## 任务输入

```text
{{task_input}}
```

<a id="expectation"></a>
## 预期结果

**可接受的可观察结果：** {{expected}}

**禁止的捷径与无效结果：** {{invalid_outcomes}}

<a id="checks"></a>
## 可运行评估

**具体检查与预期成功／失败判据：** {{checks}}

**必要人工判断与限制：** {{judgment}}
