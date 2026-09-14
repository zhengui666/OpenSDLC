# 文档约定

[English](artifacts.md) · 简体中文

流程文档统一放在仓库根目录的 `.opensdlc/`：路径固定，每项内容只保留一个权威正文，按需
创建文件。[核心流程](../SKILL.zh-CN.md)规定要做什么；本文规定语言、模板与落点，不要求填满所有文件。

<a id="root"></a>
## 根目录与标识

以当前 Git 工作树根目录为基准，可用 `git rev-parse --show-toplevel` 确认；没有 Git 时使用
明确的项目根目录。不按 shell 子目录、其他工作树或 Skill 安装位置创建 `.opensdlc/`。
同一仓库中的多个包共用根目录 `.opensdlc/`，在任务中注明受影响的包。

原样复用已有 `<task-id>`。命名**新任务**前，按下文规则解析仓库语言；任务名**必须**遵循
该语言，不按聊天语言或当前阅读的模板语言命名：

| 解析后的语言 | 新任务命名要求 | 路径示例 |
| --- | --- | --- |
| `zh-CN` | 简短的简体中文任务名 | `.opensdlc/tasks/修复登录超时/task.md` |
| `en`，含默认及回退英文 | 简短的英文任务名，小写单词用连字符连接 | `.opensdlc/tasks/fix-login-timeout/task.md` |

可以附加工单编号或必要技术名称，但不能用它们替代任务名：中文使用 `工单-128-修复登录超时`，
英文使用 `issue-128-fix-login-timeout`，而不是仅用 `issue-128`。原始外部编号保留在来源字段，
不改写外部工单或其编号。目录名、`{{task_id}}` 及所有任务引用须一致。任务标识必须是单个
合法目录名，不含 `/`、`\`，不能为 `.` 或 `..`；shell 命令中的路径加引号。
同一任务跨会话、分支、PR 及语言切换保持原标识。已有标识即使使用另一种语言，也不自动
重命名或重复建档；翻译正文不改变任务目录。仅为真实重名增加来源前缀或简短后缀，不建立编号服务。

发布、事故、评测样例及运行标识不受任务命名语言规则约束，优先使用其原生标识；对应文件系统
名称使用小写字母、数字、连字符、下划线和点，不使用分隔符或独立的 `.`、`..`。
原始外部编号保留在正文。仅在区分不同运行确有需要时使用时间戳。

下文 `T` 表示 `.opensdlc/tasks/<task-id>`，`L` 表示选中的 `en` 或 `zh-CN`，都不是 shell 变量。
`.opensdlc/...` 相对仓库根目录；模板路径相对 Skill 目录。普通 Markdown 链接相对当前文档，
填充模板时必须根据实际落点调整链接。

<a id="language"></a>
## 仓库语言

唯一语言设置位于当前仓库根目录的 `.opensdlc/config.json`：

```json
{
  "language": "en"
}
```

使用简体中文时：

```json
{
  "language": "zh-CN"
}
```

| 情况 | 行为 |
| --- | --- |
| 文件不存在，或合法 JSON 对象中缺少 `language` | 新正文与新任务标识均使用英文，不为重复默认值而创建文件 |
| `language` 严格等于 `en` | 读取 `templates/en/`，新正文与新任务标识均使用英文 |
| `language` 严格等于 `zh-CN` | 读取 `templates/zh-CN/`，新正文与新任务标识均使用简体中文 |
| JSON 非法、根值不是对象、语言值不支持或不是字符串 | 报告问题、保留原文件，新正文与新任务标识回退英文；继续不依赖该配置的工作 |
| 配置存在但无法读取 | 报告限制，新正文与新任务标识采用英文默认值，不声称已读取设置 |
| 用户明确要求修改仓库语言 | 有写入权限时仅修改 `language`，保留其他内容；新文档及新任务标识采用新值，已有任务标识不变 |
| 已有文档采用另一种语言 | 更新时保留其语言；仅在明确要求时原地翻译，不建立第二份权威正文 |

空字符串、`null`、`zh`、`zh-cn` 和 `en-US` 都不是支持的别名。未知键不是语言配置或权限，
保留而不赋予虚构行为。不支持环境覆盖、任务级语言文件、schema 服务、插件或渲染器，
也不为此偏好新增这些机制。

开始／恢复任务时读取配置；配置变化后，在创建任务或文档前重读。只读模式下说明拟使用的设置
和路径，不写入或声称已保存。不能根据聊天语言推断语言切换。设置约束新文档正文和新任务标识，
不约束聊天语言，也不另设任务标识语言选项。

**作用范围：** OpenSDLC 新任务的标识、新建的流程文档、PR／发布正文及新的产品／原生
Markdown 文档。已有仓库约定和权威文档保留其语言与结构；相关冲突须说明，不能静默翻译或覆盖。
`tasks` 等固定目录名、`task.md`／`spec.md` 等固定文件名、已有路径、机器键、代码标识符、
锚点、API 字段、命令和引用证据保持不变。生成文档应修改其源文件，不手动翻译产物。
切换语言不会批量翻译已有内容或重命名已有任务。

包内默认提供英文 `README.md`、`SKILL.md` 和参考文件，同时提供完整 `.zh-CN.md` 阅读文本。
只有根目录 `SKILL.md` 是自动发现入口。项目配置选择写作模板及参考文件的阅读语言，不改变
宿主界面、不替换已安装的 `SKILL.md`。两套模板留在 Skill 包内，项目产物每份只用一种语言。

<a id="layout"></a>
## 目录布局

```text
.opensdlc/
├── config.json                       # 可选：语言设置
├── project.md                        # 共享上下文、权威来源和原生入口
├── review.md                         # 共享审查规则
├── operations.md                     # 动作边界、交付、观察和度量
├── tasks/<task-id>/
│   ├── task.md                       # 默认单份任务记录
│   ├── intent.md                     # 仅在需要拆分时创建
│   ├── spec.md
│   ├── plan.md
│   ├── verification.md
│   ├── review.md
│   ├── handoff.md
│   └── assets/                       # 必要参考与实际截图
├── evals/
│   ├── suite.md
│   ├── cases/<case-id>.md
│   └── runs/<run-id>.md
├── releases/<release-id>.md
└── incidents/<incident-id>.md
```

这是路径表，不是初始化清单。不预建空目录、占位报告、逐步骤状态文件、`current.md` 或
成对的 `.en.md`／`.zh-CN.md` 任务记录。普通小任务仅需 `T/task.md`，共享记录按需读取或更新。

<a id="template-use"></a>
## 使用模板

创建文档前读取 `templates/L/` 下对应模板。已有权威正文或仓库模板优先；用模板补实际缺口，
而不是替换项目约定。这是普通 Markdown 编辑，不需要可执行模板引擎。

`{{snake_case}}` 是写作占位符。`{{task_id}}` 必须与[任务命名规则](#root)确定的目录名完全
一致，不能单独翻译成另一个标签。其他占位符使用所选语言填写已核实信息，删除说明性 HTML
注释和无用占位行，不需展开的章节暂不创建。显式 `<a id="..."></a>` 锚点保持不变。未知事实应写成
“未知”“待确认”或“未运行”，不能把提示变成虚构结果。YAML 键保持不变；填入带引号的值时，
正确转义引号或使用合法的块标量。

标题与字段提示是写作骨架，不是每项任务必须填完的表单。简短章节可以只有一句话。
不得为精简模板漏掉适用需求、风险、检查或责任。只有实际需要时才加入领域细节，不预建扩展设施。

不将整套模板复制到 `.opensdlc/`，只读取所需语言和相应模板。更新已有文档时先读取实际正文
与权威链接，保持既有语言。明确要求翻译时，翻译范围内全部正文，保留路径、锚点和标识符，
保留实际证据，不改变决定或批准状态。

<a id="templates"></a>
## 模板目录

每一行都有完整英文与简体中文模板。`review-policy.md` 是共享规则，`task-review.md` 是任务
审查结果；`agent-skill.md` 是新的原生 Skill 模板，不是第二个 OpenSDLC 入口。
生成文件写到规定落点，而不是写到模板库路径。

| 文档 | 固定落点 | 英文 | 简体中文 |
| --- | --- | --- | --- |
| 语言配置 | `.opensdlc/config.json` | [config.json](../templates/en/config.json) | [config.json](../templates/zh-CN/config.json) |
| 项目上下文 | `.opensdlc/project.md` | [project.md](../templates/en/project.md) | [project.md](../templates/zh-CN/project.md) |
| 共享审查规则 | `.opensdlc/review.md` | [review-policy.md](../templates/en/review-policy.md) | [review-policy.md](../templates/zh-CN/review-policy.md) |
| 共享运行实践 | `.opensdlc/operations.md` | [operations.md](../templates/en/operations.md) | [operations.md](../templates/zh-CN/operations.md) |
| 任务入口 | `T/task.md` | [task.md](../templates/en/task.md) | [task.md](../templates/zh-CN/task.md) |
| 意图 | `T/task.md#intent` → `T/intent.md` | [intent.md](../templates/en/intent.md) | [intent.md](../templates/zh-CN/intent.md) |
| 需求与设计 | `T/task.md#spec` → `T/spec.md` | [spec.md](../templates/en/spec.md) | [spec.md](../templates/zh-CN/spec.md) |
| 实现计划 | `T/task.md#plan` → `T/plan.md` | [plan.md](../templates/en/plan.md) | [plan.md](../templates/zh-CN/plan.md) |
| 验证 | `T/task.md#verification` → `T/verification.md` | [verification.md](../templates/en/verification.md) | [verification.md](../templates/zh-CN/verification.md) |
| 任务审查 | `T/task.md#review` → `T/review.md` | [task-review.md](../templates/en/task-review.md) | [task-review.md](../templates/zh-CN/task-review.md) |
| 交接 | `T/task.md#handoff` → `T/handoff.md` | [handoff.md](../templates/en/handoff.md) | [handoff.md](../templates/zh-CN/handoff.md) |
| 评测集 | `.opensdlc/evals/suite.md` | [eval-suite.md](../templates/en/eval-suite.md) | [eval-suite.md](../templates/zh-CN/eval-suite.md) |
| 评测样例 | `.opensdlc/evals/cases/<case-id>.md` | [eval-case.md](../templates/en/eval-case.md) | [eval-case.md](../templates/zh-CN/eval-case.md) |
| 评测运行 | `.opensdlc/evals/runs/<run-id>.md` | [eval-run.md](../templates/en/eval-run.md) | [eval-run.md](../templates/zh-CN/eval-run.md) |
| 发布记录与说明 | `.opensdlc/releases/<release-id>.md` | [release.md](../templates/en/release.md) | [release.md](../templates/zh-CN/release.md) |
| 事故与复盘 | `.opensdlc/incidents/<incident-id>.md` | [incident.md](../templates/en/incident.md) | [incident.md](../templates/zh-CN/incident.md) |
| 原生上下文入口 | `AGENTS.md` / `CLAUDE.md` | [native-context.md](../templates/en/native-context.md) | [native-context.md](../templates/zh-CN/native-context.md) |
| 新原生 Skill | `.claude/skills/<skill-name>/SKILL.md` / `.agents/skills/<skill-name>/SKILL.md` | [agent-skill.md](../templates/en/agent-skill.md) | [agent-skill.md](../templates/zh-CN/agent-skill.md) |
| 可复用子 Agent | `.claude/agents/<agent-name>.md` | [subagent.md](../templates/en/subagent.md) | [subagent.md](../templates/zh-CN/subagent.md) |
| 产品 README | `README.md` | [readme.md](../templates/en/readme.md) | [readme.md](../templates/zh-CN/readme.md) |
| 用户指南 | `docs/user-guide.md` | [user-guide.md](../templates/en/user-guide.md) | [user-guide.md](../templates/zh-CN/user-guide.md) |
| API 参考 | `docs/api.md` | [api-reference.md](../templates/en/api-reference.md) | [api-reference.md](../templates/zh-CN/api-reference.md) |
| 架构概览 | `docs/architecture.md` | [architecture.md](../templates/en/architecture.md) | [architecture.md](../templates/zh-CN/architecture.md) |
| 权威来源入口 | 该文档的原定固定路径 | [source-link.md](../templates/en/source-link.md) | [source-link.md](../templates/zh-CN/source-link.md) |
| PR 正文 | 原生平台 PR 正文 | [pull-request.md](../templates/en/pull-request.md) | [pull-request.md](../templates/zh-CN/pull-request.md) |

箭头表示“默认内联，需要时才拆分”，不是“同时写两份”。产品／原生路径仅在不存在适用位置
时作为默认；实际位置保留并登记到 `.opensdlc/project.md#sources` 或 `#native`。
不能因为模板存在就创建另一份文档。

<a id="task"></a>
## 任务记录与拆分

每项开发任务以 `T/task.md` 为入口。说明原始来源和交付终点：只设计、可审查 PR、合并或发布。
必要确认放在对应章节或链接实际决定，不另建批准记录。

任务稳定锚点为 `intent`、`spec`、`plan`、`verification`、`review`、`delivery` 和 `handoff`。
无论英文还是中文标题，都在标题前使用 `<a id="intent"></a>` 等显式锚点。推进到相应阶段时
再添加章节；到终点时说明适用但未完成的工作，不能通过省略暗示完成。

仅在正文较长、需独立审阅或重复引用时拆分。将正文移动到指定文件，在原章节只保留链接并
保留锚点。入口始终指向唯一正文，不能把链接存在当作阶段已完成。例如，在 `task.md` 中：

```markdown
<a id="spec"></a>
## 需求与设计

参见[规格](spec.md)。
```

任务交付继续使用 `T/task.md#delivery` 及任务模板的交付章节。正式发布采用发布模板；
仅交付 PR 的任务不需要发布记录。调研、设计决策、工作包及诊断笔记放在规格／计划／验证
章节，不默认增加 `research.md`、ADR、工作包或子 Agent 报告文件。真正独立的子任务可以
使用自己的任务标识，并与父任务互链。

只读工作在回复中提供同样结构、说明拟保存路径及尚未落盘的事实。纯问答不创建任务目录。

<a id="project-docs"></a>
## 项目共享文档

`project.md` 包含目标、架构、约定、真实构建／测试／lint 命令、健康输出、常见错误与负责人，
保持简短。`#sources` 登记实际权威需求、架构、品牌／UX、安全、产品文档、CI 与监控来源。
`#native` 登记实际上下文、Skill、子 Agent、Hook 与流水线入口，以及是否核验了发现／执行行为。

共享 `review.md` 覆盖缺陷、安全、意图／规格／计划一致性、设计原则、严重度、排除项、
人工责任与审查质量调优。已有规则保持权威；需要固定本地入口时使用 `source-link.md`。

共享 `operations.md` 的固定锚点为 `controls`、`delivery`、`observe` 和 `metrics`：分别说明
动作边界及授权路径；环境与实际部署／状态／回退／数据恢复；监测基线、确定性检测、响应层次、
真实触发与值班；采用的指标及复查周期。它不是批准数据库，也不是逐任务指标报告。

产品指南、API 文档与架构保留在登记的产品位置。包自身的 README、Skill、参考文件与模板
留在 Skill 安装目录，不复制到目标 `.opensdlc/`。

<a id="eval-docs"></a>
## 评测、发布与事故

评测接入使用 `eval-suite.md` 指向真实样例、验收检查、命令、Agent 配置、触发方式、周期、
认可基线与负责人。仅当已有可执行数据集和报告无法承载内容时使用 Markdown 样例／运行模板。
评测集引用其原生路径，不重复数据集，不导出全量日志。

发布记录包含关联任务、具体制品／环境、真实授权、准备、执行、状态核验、回退／演练、迁移、
观察及面向用户的发布说明。同次发布的多个任务共用一份记录。准备就绪不等于已部署或已获发布批准。

同一事故记录覆盖信号、影响、时间线、事实与假设、根因、实际响应与恢复、分诊决定、修复意图、
发布、复盘及永久回归样例。事故、修复任务与对应发布互链。已有发布／事故系统可保留正文，
本地使用入口引用。

<a id="native"></a>
## 原生接入位置

宿主必须发现的文件保留在其实际读取位置。沿用已启用路径，并在 `.opensdlc/project.md#native`
登记确切路径或托管入口。不创建未使用宿主的目录。

| 能力 | 原生位置／规则 |
| --- | --- |
| Claude Code 上下文 | 保留已有 `CLAUDE.md` 或 `.claude/CLAUDE.md`；需新增时默认根目录 `CLAUDE.md` |
| AGENTS.md 上下文 | 根目录 `AGENTS.md`；保留子目录作用域指令 |
| Claude Code Skill | `.claude/skills/<skill-name>/SKILL.md` |
| Codex Skill | `.agents/skills/<skill-name>/SKILL.md` |
| Claude Code 子 Agent | `.claude/agents/<agent-name>.md`；所提供子 Agent frontmatter 面向此宿主 |
| Claude Code 团队设置／Hooks | `.claude/settings.json` 或实际托管设置，不在 `.opensdlc/` 写替代配置 |
| GitHub Actions | `.github/workflows/<workflow-name>.yml`；保留已有 `.yaml` 路径 |
| 其他宿主、CI、部署、测试／评测配置 | 核实实际原生契约，登记确切路径或托管入口，不猜测 |

上下文、原生 Skill 和子 Agent **Markdown 文档**均有英中模板。Hook、CI、权限及部署的
**可执行配置**使用现有原生文件与当前官方 schema，不编造所谓跨平台配置模板。
其解释性正文由共享运行模板承载。文档语言不改变配置键和命令语法。

跨宿主优先使用已有共享分发，而非维护多份规则。由协调者将子 Agent 结果汇总回任务章节，
避免并发修改同一共享记录。宿主处于强制只读计划时，草稿先保留在宿主允许的位置；获得文档
写入权限后再归档被接受的计划。

接入时验证实际上下文／Skill／子 Agent 发现行为。创建文件或登记路径不证明宿主已加载。
宿主契约参见 [Agent Skills 规范](https://agentskills.io/specification)、
[Claude Code Skills](https://code.claude.com/docs/en/skills)、
[上下文](https://code.claude.com/docs/en/memory)、
[子 Agent](https://code.claude.com/docs/en/sub-agents)、
[设置](https://code.claude.com/docs/en/settings)与
[Codex Skills](https://developers.openai.com/codex/skills/)。

<a id="sources"></a>
## 权威来源、附件与持久化

已有工单、PR、设计系统或文档作为权威来源时，通过 `source-link.md` 或相应任务章节引用。
工作前读取实际来源，陈旧本地摘要不代表最新需求。有原生修订／提交／运行引用时直接使用，
不额外计算指纹。来源不可读时报告缺口，不将旧副本静默提升为权威。

持久流程文档按正常方式版本管理。作者与修订由 Git 或原平台保留，不逐文件维护开发日记。
各 worktree 写自己的文件，随对应变更合并。共享项目规则仅在确有需要时更新。

必要设计参考与实际截图使用 `T/assets/<descriptive-name>.<ext>`，注明用途，不能用参考图
冒充运行证据。发布／事故附件分别使用 `.opensdlc/releases/<release-id>/assets/` 与
`.opensdlc/incidents/<incident-id>/assets/`。已有平台制品直接引用，不复制缓存、全量日志
或大型二进制。不保存凭据、敏感个人信息或未脱敏生产数据。

恢复时读取原 `task.md` 及权威链接，然后检查当前分支、工作区、CI、审查与外部动作。
标题或旧完成声明不能替代事实。移动权威正文时更新链接、保留原生历史，不遗留两份可编辑权威正文。
