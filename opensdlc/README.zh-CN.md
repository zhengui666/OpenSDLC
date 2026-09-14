# OpenSDLC

**面向 AI Coding Agent 的完整软件交付流程，从明确意图到实际验证的交付，再接回运行反馈。**

[English](README.md) · 简体中文

[开始使用](#quickstart) · [语言设置](#language) · [工作流程](#workflow) · [模板](#templates) · [示例](#examples) · [文档导航](#docs)

OpenSDLC 是一个纯指令型 Agent Skill。它使用项目已有工具，连接需求、设计、实现、测试、
审查、发布与维护。工作记录放在仓库的 `.opensdlc/` 固定位置，下一位开发者或 Agent
不依赖完整聊天记录也能理解和接手。

```text
规划 → 设计 → 构建 ⇄ 测试 → 交付 → 维护
 ↑                                  │
 └────────── 实际反馈形成新意图 ──────┘
```

**先理解，再修改。** 读取真实流程，复用已有能力，修复根因。  
**实际验证，再报告。** 区分实现完成、检查通过、PR 合并与真实部署。  
**只写一份，随时可找。** 固定路径与双语模板让跨会话记录可以继续使用。

<a id="quickstart"></a>
## 开始使用

### 安装 Skill

将完整 `opensdlc/` 目录复制到 Agent 的项目级 Skill 目录，保留 `SKILL.md`、参考文件和
两套模板的相对位置。不需要安装运行时、生成器、后台服务或新项目依赖。

也可以使用 [skills.sh](https://skills.sh) CLI，将它直接安装到自动检测到的 Agent Skill 目录：

```sh
npx skills add https://github.com/zhengui666/OpenSDLC --skill opensdlc
```

| Agent | 项目级安装目录 | 显式调用 |
| --- | --- | --- |
| [Claude Code](https://code.claude.com/docs/en/skills) | `.claude/skills/opensdlc/` | `/opensdlc` |
| [Codex](https://developers.openai.com/codex/skills/) | `.agents/skills/opensdlc/` | `$opensdlc` |

**首次安装** Claude Code Skill 时，在解压后包含 `opensdlc/` 的目录执行：

```sh
PROJECT="/absolute/path/to/your-project"
mkdir -p "$PROJECT/.claude/skills"
cp -R opensdlc "$PROJECT/.claude/skills/"
```

Codex 改用 `$PROJECT/.agents/skills/`。目标已存在时，先检查并保留项目自定义内容，再替换
文件。其他宿主使用其原生加载方式，不假设所有 Agent 都扫描同一路径。没有加载器时，
显式读取 `SKILL.md` 及其引用资源。

### 发起任务

在目标仓库调用 OpenSDLC，描述目标与交付边界：

```text
使用 OpenSDLC 修复登录请求超时后页面一直加载的问题。
检查真实请求流程和已有测试，修复根因并补上回归验证。
任务标识遵循仓库语言配置。交付可审查 PR，不合并、不部署。
```

Agent 读取项目规则与相关代码，查找已有任务，并使用任务模板维护
`.opensdlc/tasks/fix-login-timeout/task.md`。必要决定完成后继续实现、验证并处理适用审查。
即使用其他语言提出请求，正文和新任务标识仍默认英文；配置为 `zh-CN` 时，该新任务改用
`.opensdlc/tasks/修复登录超时/task.md`。用一个真实小任务验证发现、文档写入和实际检查；
目录已复制不代表接入已生效。

<a id="language"></a>
## 语言设置

**默认英文。通过一个仓库设置使用简体中文。**

需要中文文档和中文新任务标识时，在**目标仓库根目录**创建或修改 `.opensdlc/config.json`：

```json
{
  "language": "zh-CN"
}
```

英文使用 `"en"`。文件或 `language` 缺失时无需配置，直接采用英文。
可用示例：[英文](templates/en/config.json) · [简体中文](templates/zh-CN/config.json)。
已有配置时合并语言设置，不覆盖无关字段。

该设置同时决定**新文档正文和新任务标识的语言**：

| 仓库语言 | 新任务标识要求 | 规格路径示例 |
| --- | --- | --- |
| `zh-CN` | 必须为简体中文，例如 `修复登录超时` | `.opensdlc/tasks/修复登录超时/spec.md` |
| `en`、未配置或回退英文 | 必须为英文，例如 `fix-login-timeout` | `.opensdlc/tasks/fix-login-timeout/spec.md` |

可附加工单编号，例如 `工单-128-修复登录超时` 或 `issue-128-fix-login-timeout`。
`tasks` 等固定目录名、`spec.md` 等固定文件名、锚点、配置键与可执行语法不变。
已有任务在配置切换后保留原标识和路径；已有文档保持其语言，除非明确要求翻译。
不生成双份记录，不改写已安装的 Skill。聊天语言独立于此设置。

包内默认 `README.md`、`SKILL.md` 和参考文件均为英文，并提供完整中文阅读文本。
根目录 `SKILL.md` 保持唯一自动发现入口。此设置是 OpenSDLC 的指令约定，不意味着宿主
原生识别 `.opensdlc/config.json`；由 Agent 在工作流中读取。
完整规则及非法值、只读模式见[语言约定](references/artifacts.zh-CN.md#language)。

<a id="workflow"></a>
## 工作流程

| 阶段 | Agent 的责任 | 有用产物 |
| --- | --- | --- |
| 规划 | 明确问题、用户、结果、约束与非目标，取得相应意图决定 | 被接受的意图 |
| 设计 | 联合定义需求与设计，解决冲突，明确验收、接口、数据、UX 与失败行为 | 可实施规格 |
| 构建 | 只读勘察、复用代码、确认计划、小步实现，隔离真正独立的工作 | 当前计划与实现 |
| 测试 | 运行反馈检查、复现缺陷、验证真实行为，评测相关 Agent 配置变化 | 实际验证与评测结果 |
| 交付 | 修复审查问题及失败 CI，完成必要审查／授权，在范围内部署并验证回退 | 实际 PR、合并或发布结果 |
| 维护 | 确定性检测信号，诊断、分诊、修复、核实恢复并保留事故回归 | 运行经验与新意图 |

上下文、可复用 Skills、子 Agent、Hooks 和 CI/CD 支持这些阶段。按触发条件使用能力：
不在每个任务中重复接入，不强行并行，不为仅交付 PR 的任务执行生产操作。
必要但缺少工具或访问的能力是未完成项，不能静默当成不适用。

需求负责人决定意图与规格，工程负责人接受计划，代码负责人审查，发布负责人授权生产操作。
一人可承担多个角色。复用已有明确决定，不逐文件或命令再次询问；Agent 不能批准自己的工作。

<a id="templates"></a>
## 文档模板

每类已定义文档均提供完整英文与简体中文模板，包含具体章节和填写提示，不是空标题或
预填的成功声明。

| 范围 | 所含模板 |
| --- | --- |
| 项目共享说明 | 项目上下文、审查规则与运行实践 |
| 任务交付 | 紧凑任务、意图、需求／设计、计划、验证、任务审查与交接 |
| Agent 评测 | 评测集、样例与运行结果 |
| 发布与维护 | 发布准备／执行／说明；事故诊断／恢复／复盘 |
| 原生 Agent 文档 | `AGENTS.md`／`CLAUDE.md` 上下文入口、新 `SKILL.md`、可复用子 Agent |
| 产品与协作 | README、用户指南、API 参考、架构、PR 正文及权威来源入口 |

从[完整模板目录](references/artifacts.zh-CN.md#templates)开始，或直接查看
[英文任务模板](templates/en/task.md)／[中文任务模板](templates/zh-CN/task.md)。
`{{snake_case}}` 是写作提示，填写事实并删除无用提示。不需要安装模板渲染器。
已有权威文档与仓库特定模板优先。

**有模板不代表必须生成所有文档。** 小任务通常只需一份 `task.md`，随着工作推进添加简短
章节。只有正文较长、需独立审阅或复用时才拆分；固定入口指向唯一正文，不保留第二份完整内容。

<a id="artifacts"></a>
## 工作内容保存在哪里

**Skill 目录存指令和模板，目标仓库的 `.opensdlc/` 存工作产物。**

```text
.opensdlc/
├── config.json                       # 可选语言偏好
├── project.md                        # 共享上下文与权威来源
├── review.md                         # 共享审查规则
├── operations.md                     # 边界、交付、观察与度量
├── tasks/<task-id>/
│   ├── task.md                       # 默认单份记录
│   ├── spec.md                       # 仅在拆分时创建
│   ├── plan.md                       # 仅在拆分时创建
│   └── assets/                       # 必要参考／真实截图
├── evals/
│   ├── suite.md
│   ├── cases/<case-id>.md
│   └── runs/<run-id>.md
├── releases/<release-id>.md
└── incidents/<incident-id>.md
```

意图、验证、任务审查与交接也各有固定拆分路径。[完整文档约定](references/artifacts.zh-CN.md)
将每类文档对应到模板与落点。按需创建目录，不预建空骨架。已有工单、PR、设计工具、CI 与
事故系统可以继续作为权威来源，本地固定入口只链接，不复制正文。

宿主发现的文件保留原生位置。产品文档保留已有产品布局。Markdown 模板承载相应正文；
可执行 Hooks、CI 与权限复用实际原生配置，不创造一套假定通用的配置格式。

<a id="examples"></a>
## 使用示例

### 交付功能

```text
使用 OpenSDLC，为设置页面增加通知偏好管理。
读取并复用账户、权限与设置模块。
明确验收与计划，完成实现、验证和审查修复。
文档遵循仓库语言配置。交付可审查 PR，不合并、不部署。
```

### 恢复任务

```text
使用 OpenSDLC，继续 .opensdlc/tasks/fix-login-timeout/。
读取任务入口与交接，再核实工作区、远端 PR 和 CI 状态。
从未完成处继续，保持原定终点；不要新建任务或重写已有记录。
```

### 切换文档语言

```text
将本仓库 OpenSDLC 文档语言设置为简体中文，配置写入 .opensdlc/config.json。
新文档使用 templates/zh-CN/ 模板，新任务标识必须使用简体中文。
保留已有文档的语言、文件名及已有任务标识。
```

### 评测 Agent 变化

```text
使用 OpenSDLC，改进本仓库的 Agent 审查指令。
读取现有规则、代表任务与认可基线，运行适用评测。
检查退化与误报，再提交配置及实际结果。
无法执行时说明缺口，不用产品单测替代 Agent 评测。
```

<a id="faq"></a>
## 常见问题

### 这是一个新的开发平台吗？

不是。OpenSDLC 是 Markdown 指令、参考文件、模板及简短 JSON 语言示例，复用 Git、工单／PR
平台、测试、CI、权限、部署与监控。不安装后台服务、不提供外部权限，也不引入策略引擎。

### 每个修改都要创建完整文档集吗？

不需要。使用单份任务入口与理解、验证和交接所需的章节，已有来源直接引用。
文档可以精简，适用检查不能因此删掉。

### 能否自主推进？

可以在已接受目标、计划与权限范围内推进。重大决定、必要人工审查及生产授权仍由有权人员
处理。Skill 指令不覆盖实际权限。

### 切换语言会翻译整个仓库吗？

不会。它决定新文档正文和新任务标识的语言。已有任务保留原标识和路径；已有内容沿用当前
语言，除非要求原地翻译。固定文件名、代码标识符、锚点及原生设置保持不变。

### 是否保证每个 Agent 都能完整执行？

不保证。入口遵循 [Agent Skills 格式](https://agentskills.io/specification)，但实际执行取决于
宿主、模型、工具与项目环境。请在实际环境核验行为。未运行检查、缺失审查和未完成的部署／
观察不能写成成功。

<a id="docs"></a>
## 文档导航

| 内容 | 英文 | 简体中文 |
| --- | --- | --- |
| 生命周期执行指令 | [SKILL.md](SKILL.md) | [SKILL.zh-CN.md](SKILL.zh-CN.md) |
| 语言、模板与固定路径 | [Artifact conventions](references/artifacts.md) | [文档约定](references/artifacts.zh-CN.md) |
| 自动化、评测、审查、发布与回流 | [Engineering operations](references/operations.md) | [工程实践](references/operations.zh-CN.md) |

包的结构如下：

```text
opensdlc/
├── README.md
├── README.zh-CN.md
├── SKILL.md                          # 唯一自动发现入口
├── SKILL.zh-CN.md                     # 完整中文阅读文本
├── references/
│   ├── artifacts.md
│   ├── artifacts.zh-CN.md
│   ├── operations.md
│   └── operations.zh-CN.md
└── templates/
    ├── en/                           # 默认文档模板与 config.json
    └── zh-CN/                        # 对应中文模板与 config.json
```
