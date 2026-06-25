# 学习指南定稿 Checklist

整合完成、用户 Review 前逐项核对。

## 流程门控

- [ ] Phase 1：`run.meta.json` 状态 `completed`（或目标 batch 均已 ok）
- [ ] Phase 1：已先运行 stage-1 skeleton manifest，且仅包含 `overview-skeleton` / 必要的 `slide-skeleton-*`
- [ ] Phase 1：已通读 stage-1 raw 并产出 `stage1-summary.md`，stage-2 manifest 基于该摘要生成
- [ ] Phase 1：已运行 stage-2 module expansion / concept breakdown，并产出 `focus-map.md`
- [ ] Phase 1：核心/难点已按 focus map 补 stage-3 `deep-dive-*`、`examples-*` 或 `visual-explain-*`
- [ ] Phase 1：`misconceptions-*`、`project-bridge`、`glossary-raw` 只在 stage-2/3 显示确有价值时作为 optional stage-4 或整合项追加
- [ ] Phase 1：课件专用 batch 已明确“仅限指定课件”，并覆盖 `slide-skeleton-*` 与必要的 `slide-module-detail-*`
- [ ] Phase 1：正式 batch 默认 `clear_conversation: true`；上一轮 summary / focus map 已显式写入下一阶段 prompt 或 manifest metadata
- [ ] Phase 1.5：已通读该模块全部 `*.answer.md`
- [ ] Phase 1.5：`notebooklm-raw/<module>/knowledge-graph.md` 已产出
- [ ] 指南章节可追溯到知识图谱节点与 raw batch
- [ ] 用户 Review 前已完成至少一轮内部「整合 → Review → 迭代整合 → Review」

## 认知与叙事

- [ ] 指南已按 `guides/学习指南框架模板.md` 搭建统一框架
- [ ] 标题和开头已说明 Part / Week 范围定位、真实课程主线与知识图谱路径
- [ ] 已列出“本指南要回答的问题 / 学习目标”
- [ ] 每个大模块有**全景节**（先讲图形问题、学完能做什么）
- [ ] 核心知识大节有「叙事线」总览
- [ ] 每个子节有「本节要回答」
- [ ] 核心章节包含概念解释、公式 / 图示 / 例子、易混点、小结与承接
- [ ] 相邻子节有「小结 → 承接」
- [ ] 读者能说出「为什么要学下一节」

## 内容与风格

- [ ] 术语表覆盖本 Part 首次出现的专业术语、算法名、缩写、坐标空间和矩阵名
- [ ] 正文首次出现专业术语时已解释，并采用 `中文(English)`；缩写采用 `Abbr(Full English Name，中文对照)`
- [ ] 每个核心公式/矩阵附符号表、坐标系位置与几何意义
- [ ] 公式、矩阵、参数方程、齐次坐标点/向量表示等非代码数学内容已用 LaTeX 渲染，而不是行内代码或 `text` 代码块
- [ ] 难点有视觉直觉、数值例子或小图示
- [ ] ≥2 组易混概念对比表
- [ ] ≥3 处「追问」或「直观理解」块
- [ ] ≥3 张 Mermaid/ASCII 图（渲染管线、坐标链、算法流程等）
- [ ] 重难点不只给定义，已补示例、例题、直观解释或形象比喻
- [ ] 合适章节已串联前后周、课件模块、Project 或考试复习路径
- [ ] 关键结论可追溯到来源，且核心章节附近有简短 `参考来源` 引用块
- [ ] `参考来源` 主体是可读的 Week 课程记录、课件标题、论文标题或 Project / Assignment 文档标题，而不是 `*.answer.md` 文件名
- [ ] 无法还原标题时已写「对应 Week 记录/课件（标题待校准）」并保留 `raw batch: ...` 辅助追溯
- [ ] 最终指南没有末尾集中大“资料索引”表；完整映射已留在知识图谱或 review/iteration 文档
- [ ] 最终指南没有 `Step 4 补充采集说明`、补采计划、manifest 计划或 NotebookLM 执行命令；这些内容已移到 raw/review/iteration 文档
- [ ] Markdown 表格安全：表格单元格内没有未转义竖线，例如将竖线绝对值写法改为 `abs(m)`
- [ ] 课纲偏差已标注
- [ ] 与前后周 / Project 桥接在 L4 体现

## 技术

- [ ] NotebookLM 认证有效（`sync-auth.py --check` + 代理）
- [ ] WSL 代理已生效：`HTTP_PROXY`、`HTTPS_PROXY`、`http_proxy`、`https_proxy` 指向 `http://127.0.0.1:7897`
- [ ] `notebooklm-py` 采集路径已验证：`AuthTokens.from_storage()` 能 fetch csrf/session，极小 `ask` 返回 `AskResult.answer`
- [ ] `guides/CG课程-内容梳理.md` 进度已更新

## 禁止项（任一命中则未定稿）

- [ ] 未产出知识图谱即写指南
- [ ] 大模块无全景节直接推导
- [ ] 只粘贴 raw 无叙事串联
- [ ] 公式、矩阵或代码没有解释图形学意义
- [ ] 非代码公式、矩阵、参数方程或点/向量表示误用行内代码 / `text` 代码块
- [ ] 专业术语首次出现未解释，或术语表缺失核心术语
- [ ] 最终指南包含采集计划、补采说明、manifest 操作、NotebookLM 执行命令或长篇 raw 索引
- [ ] 最终指南以 `*.answer.md` 文件名作为章节引用主来源
- [ ] Markdown 表格因未转义竖线、复杂公式或长代码破坏渲染
