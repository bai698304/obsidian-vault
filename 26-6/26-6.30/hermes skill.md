# Hermes Agent 技能系统（Skills）完全指南

**生成日期**: 2026-07-01  
**来源**: 实际项目体验 + skill_view 文档拆解  
**本机路径**: C:\Users\LEGION\AppData\Local\hermes\skills\

---

## 一、技能是什么

Skills 是 Hermes 的**可复用程序性记忆（procedural memory）**——把特定任务的工作流、工具链、已知坑点打包成一个 SKILL.md 文档。每次 Hermes 启动时，扫描技能目录，匹配到的技能内容注入到 system prompt 中，告诉代理"遇到这类任务按这个流程走"。

**与传统的区别**:

| 概念 | 是什么 |
|------|--------|
| memory（记忆） | 存储**事实**（用户偏好、环境细节、工具路径） |
| skills（技能） | 存储**流程**（做某类任务的步骤、坑点、验证清单） |
| AGENTS.md | 当前项目的**硬约束规则** |
| SOUL.md | 代理的**身份/人格设定** |

**一句话**: 技能让 Hermes 能"干过一次类似的活，下次就知道怎么干"。

---

## 二、本项目实际用到的核心技能

在「认知广与认知高」3 集视频脚本项目中，以下技能直接参与了工作流程：

### 1. document-to-video-script（文档转视频脚本）

| 项目 | 内容 |
|------|------|
| **分类** | creative |
| **文件** | C:\Users\LEGION\AppData\Local\hermes\skills\creative\document-to-video-script\SKILL.md |
| **何时触发** | 当用户要求将文档/文章/对话转为视频脚本时 |

**这个技能包含了什么**：

整个管线的 10 个步骤，按顺序：

```
Step 1: 文档类型分类（意见分析/故事案例/教程/哲学对话……）
Step 2: 格式选择（师生对话体/纯口播/播客对谈/纪录片式）
Step 3: Hook 设计（黄金三秒 + 10 种钩子类型 + 场景式钩子）
Step 4: 结构重组（结论前置、每段只说一件事、15 秒节奏法则、递进式穿透、ABC 对照法、旁白与画面同步设计）
Step 5: 口语化（书面语→口语的 7 条转化规则 + 检查清单）
Step 6: 系列拆分（长文档拆成 3 集）
Step 7: 音频生成（ChatTTS API 调用）
Step 8: 脚本审核（五维审核框架）
Step 9: 创作者参考研究（渠道搜索 + 评价标准 + 优先级排序）
Step 10: 批判性基准分析（批判性分析三问框架）
```

**本项目中的实际效果**:

| 任务 | 技能的哪部分生效 |
|------|----------------|
| 研究文档转视频方法论（task-001） | Step 1-6 的所有方法论框架 |
| 诊断报告分析（diagnosis-report.md） | Step 8 五维审核框架 |
| 格式选择论证（format-proposal.md） | Step 2 格式选择矩阵 |
| ep01 脚本审核（ep01_hermes_review.md） | Step 8 的 5 个维度逐一对照 |
| 创作者参考库（creator_reference.md） | Step 9 创作者研究流程 |
| 汤质批判分析（tangzhi_critique_hermes.md） | Step 10 批判性分析框架 |

**没有这个技能会怎样**：每次接到"把文档转成视频"的任务，我得从头想该检查什么。技能把方法论、检查清单、已知坑点全部打包好了。

---

### 2. web-research-report（多平台搜索→结构化报告）

| 项目 | 内容 |
|------|------|
| **分类** | research |
| **何时触发** | 用户要求研究某个主题并写报告时 |

**包含内容**：

- **多平台搜索策略**: 推荐同时发多个中文查询（加"方法论""工作流""经验"等关键词）
- **工具容错方案**: 这个技能记录了 `web_extract` 在 DuckDuckGo 后端下不可用、`browser_navigate` 在 Windows 上有 Win32 错误。提供了 Python urllib 回退脚本（直接复制粘贴就能跑的代码）
- **报告结构模板**: 提供了标准化的 markdown 报告大纲

**本项目中的实际效果**:

| 场景 | 技能做了什么 |
|------|------------|
| task-001 方法论文献研究 | 指导了搜索关键词设计 + 多轮查询策略 |
| 搜索时 web_extract 失败 | 技能预置了的回退方案（Python urllib），直接执行，没有卡住 |
| 创作者查找 | 技能提供了"每个平台换关键词"的多路搜索策略 |

**没有这个技能会怎样**：第一次 web_extract 失败后我可能需要多试几次才切换方案。技能直接告诉我"这个后端不支持提取，换 Python urllib"，节省了试错时间。

---

### 3. hermes-agent（Hermes 自身操作指南）

| 项目 | 内容 |
|------|------|
| **分类** | autonomous-ai-agents |
| **文件** | skills\autonomous-ai-agents\hermes-agent\SKILL.md（3.5 万字） |
| **何时触发** | 涉及 Hermes 配置、CLI 命令、界面操作时 |

**包含内容**：

- CLI 命令大全（chat / config / sessions / skills / cron / gateway / mcp 等所有子命令）
- Slash 命令参考（/new / /model / /title / /resume 等）
- 会话管理（自动保存 + hermes -c / hermes --resume / hermes session list）
- 项目上下文文件系统（AGENTS.md / CLAUDE.md / .hermes.md 的加载规则）
- Windows 特有坑点（UTF-8 BOM、Alt+Enter 新行、WinError 10106）
- 代理衍生（spawn / delegate / tmux 多代理）

**本项目中的实际效果**:

| 场景 | 技能做了什么 |
|------|------------|
| 你问 AGENTS.md 加载规则 | 技能直接给出了 AGENTS.md 的查找规则和优先级 |
| 你问会话管理命令 | 技能包含了 hermes -c / hermes --resume / hermes sessions list 等完整命令参考 |
| 你问技能系统原理 | 技能本身就在说明 Hermes 的技能机制 |

**没有这个技能会怎样**：当你问"Hermes 有哪些会话管理命令"时，我得去查文档或靠推测回答。技能把这些信息直接嵌在 system prompt 里。

---

## 三、其他可用技能一览（共 64 个）

本机安装了 64 个技能，分 12 个类别。以下是与本项目最相关、或值得了解的：

### 内容创作类

| 技能名 | 功能 | 对本项目的价值 |
|--------|------|--------------|
| **excalidraw** | 生成手绘风格架构图/流程图/时序图 | 知识四层结构图可以用它画 |
| **sketch** | 快速 HTML 界面原型（2-3 个方案对比） | 做视频封面/缩略图 A/B 测试 |
| **humanizer** | 去除 AI 痕迹，添加真实语气 | 脚本口语化改写的辅助工具 |
| **baoyu-infographic** | 21 种布局 × 21 种风格的信息图 | 知识四层/精致穷人对比图的设计参考 |

### 研究类

| 技能名 | 功能 |
|--------|------|
| **arxiv** | 搜索 arXiv 论文（按关键词/作者/分类） |
| **blogwatcher** | 监控博客/RSS 更新 |

### 数据/实验类

| 技能名 | 功能 |
|--------|------|
| **spike** | 快速实验验证一个想法是否可行 |
| **plan** | 写分步执行计划（不执行，只输出 markdown） |
| **systematic-debugging** | 4 阶段根因调试法 |

### GitHub 类

| 技能名 | 功能 |
|--------|------|
| **github-code-review** | PR 代码审查 + 行内评论 |
| **github-pr-workflow** | PR 全生命周期管理 |

---

## 四、技能是如何被"触发"的

Hermes 读取技能的机制：

```
系统启动时
  └─ 扫描 ~/AppData/Local/hermes/skills/ 目录
  └─ 读取每个 SKILL.md 的 frontmatter（name / description / tags）
  └─ 进入对话后，当用户输入匹配技能的 description 语义时
       └─ 技能内容注入 system prompt
       └─ 代理在思考时能看到技能中预置的步骤、工具、坑点
```

**具体到本项目**:

当你第一次说"读取并执行 task-001-doc-type-research.md 中的研究任务"时，`document-to-video-script` 技能被检测到匹配（描述中有"converting written documents into video scripts"），然后全文注入 system prompt。之后我做的所有格式分析、hook 设计、审核工作，都在按这个技能的步骤走。

---

## 五、技能 vs 手动 prompt——效果差异

| 对比项 | 无技能（纯 prompt） | 有技能（SKILL.md） |
|--------|-------------------|-------------------|
| **步骤完整性** | 凭记忆，容易漏步骤 | 技能写了 10 步，一步不缺 |
| **检查清单** | 靠经验，不系统 | 每个步骤有明确的 check list |
| **工具容错** | 现试，失败换方案 | 预置了"这个后端不能提取，用这个 Python 代码" |
| **同行评审** | 靠直觉判断好坏 | 技能提供 5 维度审核框架，逐项打分 |
| **已知坑点** | 踩过才知 | 技能直接告诉你"15 秒节奏法则"、"结论前置" |
| **新创作者上手** | 靠自己摸索 | 技能给出 8 位同类创作者 + 每个的偷师点 |

**最直观的体验**: 当 web_extract 失败时，`web-research-report` 技能直接告诉我"DuckDuckGo 后端只能搜索不能提取，用 execute_code 跑 Python urllib"，而不是让我傻傻重试。

---

## 六、技能可以从哪里来

| 来源 | 说明 | 命令 |
|------|------|------|
| 预装 | 安装 Hermes 时自带 64 个核心技能 | 无需操作 |
| 技能中心安装 | 从公开注册表安装社区技能 | `hermes skills install <id>` |
| 自动生成 | 完成复杂任务后 Hermes 可以记住流程 | `skill_manage(action='create', ...)` |
| 手动编写 | 用户自己写 SKILL.md 放入 skills 目录 | 直接创建 .md 文件 |
| GitHub 仓库 | 添加 GitHub 仓库作为技能源 | `hermes skills tap add <repo>` |

**本项目中的案例**: 本次对话中，`document-to-video-script` 技能一直在被动更新——你提出的"画面不是配图是叙事本身"、"场景式钩子"、"递进式穿透"几个新观点，我在当前对话中使用了这些改进，但技能本身没有被更新（除非有人主动去 patch）。技能是会过时的——使用时遇到问题应当 patch 更新它。

---

## 七、对本项目的建议

如果你以后打算反复做"文档转视频"类型的项目，可以：

1. **把本次对话中积累的新手法加到技能里**: 场景式钩子、递进式穿透、ABC 对照法、汤质批判分析框架，这些目前不在原始技能中，是你和我在本次对话中新提炼的
2. **让 Hermes 在新会话中预加载这个技能**: `hermes -s document-to-video-script` 启动时直接加载
3. **为你的项目写一个定制技能**: 如果有一组你反复使用的检查项（视频规格、ChatTTS 参数、命名规范），可以单独写一个技能挂在你的项目目录下
