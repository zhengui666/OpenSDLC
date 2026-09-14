<!-- 落点: AGENTS.md 或 CLAUDE.md（保留已有宿主支持的路径）
合并到正在使用的原生入口，不替换已有作用域规则。项目上下文保持唯一，不在此复制整个 OpenSDLC 流程。
用事实替换占位符。可删除不需展开的提示，不得删掉必要行为。模板不证明工作已经执行。 -->

# 项目指令

<a id="context"></a>
## 项目上下文

**读取当前共享上下文：** {{project_context_path}}

**相关已有作用域指令：** {{scoped_instructions}}

<a id="workflow"></a>
## 开发流程

执行生命周期任务时，读取 `{{opensdlc_skill_path}}` 的 OpenSDLC 入口。创建任务或文档前读取当前仓库根目录的 `.opensdlc/config.json`；文件或 `language` 缺失时使用 `en`，`zh-CN` 选择简体中文模板。新任务标识在 `zh-CN` 时必须用简体中文（修复登录超时），`en`、默认或回退英文时必须用英文（fix-login-timeout）。已有任务标识及固定文件名不变。未要求翻译时保留已有文档语言。复用任务入口及原生测试，不重复建档。

<a id="boundaries"></a>
## 本地约束

**其他位置尚未说明的项目约束：** {{local_constraints}}
