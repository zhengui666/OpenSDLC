<!-- 落点: .opensdlc/operations.md
只写项目实际控制与命令。它是共享操作说明，不是批准数据库。能力进入范围时再增加相应运行章节。
用事实替换占位符。可删除不需展开的提示，不得删掉必要行为。模板不证明工作已经执行。 -->

# 项目运行实践

<a id="controls"></a>
## 动作边界

| 受限动作 | 原生控制位置 | 负责人／授权入口 | 阻止后可继续路径 |
| --- | --- | --- | --- |
| {{action}} | {{control_location}} | {{authorization_route}} | {{continuation}} |

**实际检查的允许／拒绝行为：** {{control_checks}}

<a id="delivery"></a>
## 交付与恢复

**环境与自治范围：** {{environments}}

**部署／状态／回退命令、目录与接口：** {{deployment_commands}}

**自动化身份、隔离与凭据来源；不写密钥值：** {{automation}}

**数据迁移、恢复与旧版兼容：** {{data_recovery}}

**回退演练入口、实际结果与周期：** {{rehearsal}}

**发布后行为与观察标准：** {{post_deploy}}

<a id="observe"></a>
## 观察与响应

**信号、基线与确定性检测规则位置：** {{signals}}

**记录／诊断／受限响应及允许的操作手册：** {{response_levels}}

**实际调度／webhook／服务触发器：** {{triggers}}

**服务负责人、值班、分诊与沟通入口：** {{on_call}}

**事故、修复任务与永久回归位置：** {{feedback}}

<a id="metrics"></a>
## 度量与改进

**采用的过程与结果指标；已有数据源：** {{measures}}

**负责人、复查周期与可执行改进：** {{metrics_review}}
