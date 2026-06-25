# CG Week 1-2 内部 Review 与迭代记录

> **对象**：`guides/CG-Week1-2-学习指南.md`  
> **依据**：`notebooklm-raw/week1-2/knowledge-graph.md` 与 `runs/latest/*.answer.md`  
> **日期**：2026-06-25

## Draft 0：基础框架

按 `knowledge-graph.md` 的认知阶梯建立章节：

1. 术语表
2. 知识地图
3. CG 学科与应用
4. 渲染管线
5. 扫描转换
6. 数学语言
7. 重难点与串联

## Review 1：发现的问题

| 问题 | 风险 | 处理 |
|------|------|------|
| 原规划容易把 P1 写成“总览 + 数学基础”，弱化 Week 2 扫描转换 | 与 raw 不一致，遗漏 Bresenham、DDA、曲线、多边形填充 | 将扫描转换提升为核心章节 `2.3` |
| raw 中关于矩阵/齐次坐标与课件02存在来源差异 | 误导读者以为 Lecture02 已完整推导矩阵 | 在 `2.4` 增加课纲注，明确这是 Week 2 笔记/后续承接 |
| 管线术语容易停留在定义 | 读者无法调试片元、framebuffer、深度测试问题 | 加入三角形数据流和“片元不是像素”追问块 |
| DDA/Bresenham 对比缺少可操作公式 | 学习指南变成概念对比，不能复习算法 | 加入决策参数公式和更新规则 |
| Project 信息不足 | 可能编造作业细则 | 只写 raw 可确认的环境搭建、AI 互动记录、复习落点，并标注缺 Project 文档 |

## Draft 1：迭代后的关键改动

- 新增 Mermaid 管线图、坐标空间链路图、知识地图图。
- 将 `misconceptions-part1` 整合为易混点表和重难点解释。
- 将 `examples-pipeline-and-math` 改写为 Bresenham 可复习公式，不直接粘贴 raw。
- 增加 3 个固定块：`追问：为什么第一周讲应用第二周讲画线`、`直观理解：片元不是像素`、`追问：为什么不用普通坐标直接写 x+tx`。
- 在资料索引中保持每节可追溯到 raw batch。

## Review 2：Checklist 自检

| 检查项 | 状态 | 说明 |
|--------|------|------|
| Phase 1 completed | 通过 | `run.meta.json` 为 completed，12/12 ok |
| Phase 1.5 知识图谱 | 通过 | 已生成 `knowledge-graph.md` |
| 大模块全景节 | 通过 | `知识地图` 与每个核心小节的叙事线提供全景 |
| Mermaid/ASCII 图 | 通过 | 3 张 Mermaid 图 |
| 易混对比 | 通过 | DDA/Bresenham、主步进轴、扫描线/区域填充、点/向量等 |
| 追问/直观理解块 | 通过 | 3 处 |
| 来源可追溯 | 通过 | `资料索引` 与知识图谱 batch 映射 |
| 课纲偏差标注 | 通过 | 标注课件02未完整讲矩阵/齐次坐标 |
| Project 细节 | 有缺口 | 缺独立 Project/评分文档，未补采 |

## 后续建议

- 用户确认 Project/作业文档上传后，补采 `supplement-project-rubric-part1`。
- 若要面向考试训练，补采或手工构造完整 Bresenham 决策参数表。
