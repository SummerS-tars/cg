# CG Week 7-9 内部 Review 与迭代记录

> **对象**：`guides/CG-Week7-9-学习指南.md`  
> **依据**：`notebooklm-raw/week7-9/knowledge-graph.md` 与 Stage 1-3 `*.answer.md`  
> **日期**：2026-06-25

## Draft 0：基础框架

按知识图谱建立章节：

1. 术语表
2. 知识地图
3. Fragment Shader 数据流
4. 局部光照与 Phong / Blinn-Phong
5. Microfacet BRDF
6. Flat / Gouraud / Phong Shading
7. Texture Mapping、Filtering 与纹理应用
8. 易混点、复习路线与前后承接

## Draft 1：基础补充

- 从 Stage 2 raw 补齐 local illumination、BRDF、shading interpolation、shader data flow、texture mapping、filtering / applications 的基础解释。
- 将核心术语按英语考试格式写入术语表，例如 `BRDF(Bidirectional Reflectance Distribution Function，双向反射分布函数)`、`LOD(Level of Detail，细节层次)`。
- 在核心章节末尾加入 `参考 raw` 引用块，避免最终指南末尾集中堆资料索引。

## Draft 2：重难点深挖

- 依据 Stage 3 raw 加入 fragment shading 数据流 Mermaid、Phong / Blinn-Phong 公式、高光指数数值例、Microfacet D/F/G 视觉解释、Texture Filtering 和 Mipmap 直觉。
- 对 Stage 2/3 texture raw 中 UV 范围的引用排版噪声做审计：原回答出现 `$[8]$` 或 `[4]`，指南中改为图形学常规定义 $[0,1]$。
- 将 Visibility / HSR 内容压缩为 P3 承接，不重复 P3 的 Z-buffer 大章。

## Draft 3：可视化与串联

- 加入 5 张 Mermaid 图：P4 知识地图、fragment shader 数据流、Microfacet D/F/G、texture mapping、复习路线。
- 通过“P3 决定 fragment 能否留下，P4 决定 fragment 是什么颜色”串联前后 Part。
- Project / GLSL 代码框架未在 source list 中单独出现，因此不写具体 API 教程或作业实现。

## Review 1：质量标准自检

| 检查项 | 状态 | 说明 |
|--------|------|------|
| 术语首次解释 | 通过 | 核心术语均在术语表和正文首现附近解释 |
| 英语考试术语格式 | 通过 | 使用 `中文(English)` 或 `Abbr(Full English Name，中文对照)` |
| 数学表达 LaTeX | 通过 | 光照公式、半程向量、Mipmap LOD 公式使用 LaTeX |
| 章节就近引用 | 通过 | 核心章节均有 `参考 raw` 块 |
| 最终指南无采集说明 | 通过 | 未加入 manifest、补采步骤或 Step 4 说明 |
| Markdown 表格安全 | 通过 | 表格内未使用未转义竖线绝对值写法 |
| Mermaid 合理 | 通过 | Mermaid 表达数据流、材质模型和复习路线 |
| 课纲偏差标注 | 通过 | HSR 压缩为 P3 承接；无 GLSL / Project source 时不扩写 |

## Optional Stage 4 决策

不追加 optional stage-4。Stage 1-3 已覆盖 P4 主线；Project / GLSL 代码框架 source 未单独出现，强行追问容易脱离 raw。后续若用户上传 shader 代码或作业框架，可用 `supplement-*` 单独补采。

## 并行调度记录

用户建议在批量推进多个 Part 时，NotebookLM raw 采集保持串行，但某个 Part raw 完成后的 knowledge graph / guide / review 整理可与下一个 Part raw 采集交错推进。本轮 P3 已在进入 P4 前完成提交推送，P4 未与 P3 混合提交；该经验已沉淀到 `.cursor/skills/cg-course-notebooklm/docs/raw-data.md`。

## 后续建议

- 用户 Review 时若需要考试练习，可追加独立题单，重点覆盖 Phong / Blinn-Phong 公式、Microfacet D/F/G、Flat/Gouraud/Phong 对比、UV / mipmap / normal mapping。
- 若后续补齐 shader 代码或 Project 文档，再补采 shader data flow 与具体调试关联 raw。
