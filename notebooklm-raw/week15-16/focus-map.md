# Week 15-16 / Part 7 Focus Map

> **生成时间**：2026-06-26  
> **输入 run**：`notebooklm-raw/week15-16/runs/20260626-023329`  
> **Stage 2 状态**：7/7 completed，2 retry；曲线曲面 batch 两次连接断开后重试成功。

## 1. 认知重点分级

| 主题 | 等级 | 已有 raw | 指南处理 |
|------|------|----------|----------|
| 期末范围与作业/PPT 边界 | critical | `concept-breakdown-exam-homework-boundary` | 放在指南开头，明确可确认考点与不可推断内容 |
| Alpha 混合 / 颜色科学 / HDR | critical | `concept-breakdown-alpha-color-display` | Alpha 公式必考，给数值例；颜色科学作显示背景 |
| 参数曲线 / 曲面 / NURBS | critical | `concept-breakdown-curves-surfaces` | 作为 Week16 新增核心，补 P5 几何建模缺口 |
| 渲染管线 / MVP / Shader / Buffer | critical | `concept-breakdown-pipeline-programmable-api` | 作为总复习主轴，用管线图串起 P1-P6 |
| GPU-driven rendering / Mesh Shader / Visibility Buffer | important | `concept-breakdown-gpu-driven-rendering` | 作为工业前沿，强调逻辑理解而非死记细节 |
| VR / 空间智能 / AI 工具趋势 | important | `concept-breakdown-vr-spatial-intelligence` | 分清考试核心与行业展望，放在收束章节 |
| 光线追踪 / Path Tracing / AI 降噪 | important | `concept-breakdown-raytracing-review` | 作为 P6 复习承接，不重复完整 P6 指南 |

## 2. 难点与缺口

1. **考试边界必须保守**：已确认“PPT + 作业内容会考”，但没有题型、分值、Project 展示流程或详细 rubric。
2. **Alpha 公式要给正确范围**：Stage 2 raw 中 `$\\alpha$ 取值范围` 被引用编号污染为 `$[4]`，指南需修正为 $\\alpha \\in [0,1]$。
3. **曲线曲面需要直觉与公式并重**：控制顶点、基函数、节点向量、权重和连续性不能只列名词。
4. **管线复习要从数据流讲**：CPU 端应用阶段、MVP、顶点着色器、光栅化、片元着色、深度/混合、framebuffer 需要一张完整图。
5. **GPU-driven 与传统管线容易混淆**：需要对比 CPU 提交 draw call 与 GPU 自主 culling / LOD / indirect draw。
6. **VR / 空间智能属于收束与展望**：除了非对称投影、Alpha 投影融合等可考知识，其余应标为行业趋势。
7. **Local Shading 偏差**：边界审计 raw 把“Part 7”误解为 Lecture 7 Local Shading；Blinn-Phong 只作为作业 / P4 复习点，不作为 P7 新授主线。

## 3. Stage 3 目标

Stage 3 只对指南最需要图示、例题和易混对比的点补 raw：

1. `examples-alpha-blending-exam`：补 Alpha 混合数值例、投影融合例和考试表达方式。
2. `visual-explain-pipeline-mvp-shader`：补完整渲染管线 + MVP / Shader / Buffer 数据流图。
3. `deep-dive-curves-nurbs-continuity`：补 Bezier / B-spline / NURBS / C0-C2 连续性的直观对比。
4. `compare-traditional-gpu-driven-pipeline`：补传统管线 vs GPU-driven / Mesh Shader / Visibility Buffer 对比。
5. `review-map-final-exam-p1-p6`：补 P1-P6 复习地图，明确可确认考点和资料边界。
6. `visual-explain-vr-spatial-ai`：补 VR / 分布式渲染 / 空间智能 / AI 工具趋势的收束链路图。

## 4. Optional Stage 4 判断

暂不追加 optional stage-4。Stage 1-2 已覆盖 Week15-16 主线；Project 展示要求和 rubric 是资料缺失，不应通过追问让 NotebookLM 猜测。若用户后续提供独立 Project / rubric 文档，再追加 `project-rubric-supplement`。
