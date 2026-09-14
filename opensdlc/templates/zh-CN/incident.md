<!-- 落点: .opensdlc/incidents/<incident-id>.md
诊断、恢复与复盘共用本文。区分事实与假设。恢复必须是观察到的结果，而不是调用过命令。
用事实替换占位符。可删除不需展开的提示，不得删掉必要行为。模板不证明工作已经执行。 -->

# {{incident_title}}

<a id="impact"></a>
## 信号与影响

**告警／报告、实际触发与基线：** {{signal}}

**受影响用户、服务、时长与严重度：** {{impact}}

**服务负责人／值班者与响应层次：** {{owner}}

<a id="timeline"></a>
## 时间线

| 时间与时区 | 事实／动作 | 依据 |
| --- | --- | --- |
| {{time}} | {{event}} | {{evidence}} |

<a id="diagnosis"></a>
## 诊断

**已确认事实与支持信号：** {{facts}}

**假设、验证与剩余问题：** {{hypotheses}}

**根因与促成因素，或明确未知：** {{root_cause}}

<a id="response"></a>
## 响应与恢复

**负责人实际分诊决定与授权响应：** {{decision}}

**已执行动作与当前外部状态：** {{actions}}

**指标恢复、用户行为与观察窗口：** {{recovery}}

**沟通线程与实际更新：** {{communication}}

<a id="learning"></a>
## 预防与后续

**修复意图／任务与对应发布：** {{fix}}

**永久回归样例与实际检查：** {{regression}}

**监测／上下文／操作说明改进、负责人与后续：** {{improvements}}
