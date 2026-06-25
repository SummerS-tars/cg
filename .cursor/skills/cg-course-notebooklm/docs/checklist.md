# 学习指南定稿 Checklist

整合完成、用户 Review 前逐项核对。

## 流程门控

- [ ] Phase 1：`run.meta.json` 状态 `completed`（或目标 batch 均已 ok）
- [ ] Phase 1：manifest 至少包含 Part 骨架 `overview-skeleton`，并基于其回答拆出 `concept-breakdown-*`
- [ ] Phase 1：核心/难点已按需补 `deep-dive-*`、`examples-*`、`misconceptions-*` 或 `project-bridge`
- [ ] Phase 1：课件专用 batch 已明确“仅限指定课件”，并覆盖 `slide-skeleton-*` 与必要的 `slide-module-detail-*`
- [ ] Phase 1.5：已通读该模块全部 `*.answer.md`
- [ ] Phase 1.5：`notebooklm-raw/<module>/knowledge-graph.md` 已产出
- [ ] 指南章节可追溯到知识图谱节点与 raw batch
- [ ] 用户 Review 前已完成至少一轮内部「整合 → Review → 迭代整合 → Review」

## 认知与叙事

- [ ] 每个大模块有**全景节**（先讲图形问题、学完能做什么）
- [ ] 核心知识大节有「叙事线」总览
- [ ] 每个子节有「本节要回答」
- [ ] 相邻子节有「小结 → 承接」
- [ ] 读者能说出「为什么要学下一节」

## 内容与风格

- [ ] 每个核心公式/矩阵附符号表、坐标系位置与几何意义
- [ ] 难点有视觉直觉、数值例子或小图示
- [ ] ≥2 组易混概念对比表
- [ ] ≥3 处「追问」或「直观理解」块
- [ ] ≥3 张 Mermaid/ASCII 图（渲染管线、坐标链、算法流程等）
- [ ] 重难点不只给定义，已补示例、例题、直观解释或形象比喻
- [ ] 合适章节已串联前后周、课件模块、Project 或考试复习路径
- [ ] 关键结论可追溯到来源（课程记录 / 课件编号 / 作业文档）
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
