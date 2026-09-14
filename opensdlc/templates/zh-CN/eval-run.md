<!-- 落点: .opensdlc/evals/runs/<run-id>.md
仅在没有完整权威报告时使用。引用原生运行／配置标识，不另建指纹或日志系统。
用事实替换占位符。可删除不需展开的提示，不得删掉必要行为。模板不证明工作已经执行。 -->

# {{run_title}}

<a id="run"></a>
## 运行范围

**实际运行标识／时间与运行器：** {{run}}

**候选配置与认可基线引用：** {{configurations}}

**纳入样例、实际命令与环境：** {{scope}}

<a id="results"></a>
## 实际结果

| 样例 | 基线结果 | 候选结果 | 依据／失败原因 |
| --- | --- | --- | --- |
| {{case}} | {{baseline_result}} | {{candidate_result}} | {{evidence}} |

<a id="decision"></a>
## 比较与审查

**退化、改善与噪声：** {{comparison}}

**审查者与实际决定／待决定事项：** {{decision}}

**未运行样例、限制与下一步：** {{limitations}}
