# Week 15-16 / Part 7 Stage 1 Summary

> **生成时间**：2026-06-26  
> **输入 run**：`notebooklm-raw/week15-16/runs/20260626-014343`  
> **Stage 1 batches**：`overview-skeleton`、`notes-skeleton-week15`、`notes-skeleton-week16`、`source-boundary-week16-project-rubric`  
> **状态**：4/4 completed，0 retry。  
> **Week16 source 同步**：`notebooklm-raw/source-sync/week16-周一-图形学.md` 已脱敏落盘，并以 `笔记-week16-周一-图形学` 加入 CG NotebookLM，状态 `ready`。

## 1. Stage 1 采集结论

Stage 1 重新确认 P7 的实际资料边界：NotebookLM 中可见的 P7 直接 source 已包含 **`笔记-week15-周一-图形学`** 与 **`笔记-week16-周一-图形学`**。P7 不再是“Week16 缺失”的状态。

仍然缺失的 source：

- 独立 Project / Final Project 说明书。
- 具体展示要求、Presentation 流程或 Demo 要求。
- 详细评分标准 / rubric。
- 官方系统化期末复习提纲与题型分布。

Week15-16 真实模块包括：

1. **期末考试与作业/PPT 复习边界**
   - Week15 明确 Alpha 混合公式 $I = \alpha F + (1-\alpha)B$ 为必考。
   - Week16 明确考试题目来自课堂 PPT，重点考作业涉及内容：渲染管线、Blinn-Phong、MVP 矩阵传递、Shader 编写、Buffer 绑定、Vulkan / OpenGL 流程。
   - 作业完成情况是成绩重要组成部分，但未给详细 rubric。
2. **Alpha 混合、颜色科学与显示**
   - Week15 讲 Alpha 通道和投影融合 / 边缘融合。
   - Week15/16 涉及颜色感知、锥状细胞 / 杆状细胞、RGB 加色模型、HDR 与显示增强。
3. **空间智能、AI 工具与图形学趋势**
   - Week15 讨论 World Labs、空间智能、高保真仿真、Coding Agent、AIGC 对图像处理工具的影响。
   - 该模块是应用展望和学习方法，不是 Project rubric。
4. **VR / AR 与分布式渲染**
   - Week15 讲 VR 视网膜级分辨率、纱窗效应、多机分布式渲染、几何校正和边缘融合。
   - Week16 回顾 VR 立体视觉和非对称投影矩阵。
5. **参数曲线与参数曲面**
   - Week16 讲参数曲线、基函数、控制顶点、分段参数多项式、Bezier、B-spline、NURBS、张量积曲面、连续性和工业 CAD 难点。
   - 这是 P5 几何建模缺口的重要补齐。
6. **渲染管线与可编程 API 总复习**
   - Week16 回顾应用阶段、几何处理、光栅化、像素处理、深度 / 模板 / 混合。
   - 强调齐次坐标、MVP、Shader、描述符集、Buffer 绑定与 Vulkan / DX12 的手动管线配置。
7. **GPU-driven rendering 与工业资料**
   - Week16 讲 Mesh Shader、Meshlet、Visibility Buffer、CPU-GPU 通信瓶颈和 Ubisoft 2015 GPU-driven rendering 资料。
   - 关联《赛博朋克 2077》光线追踪工业文档。
8. **光线追踪、路径追踪与 AI 降噪**
   - Week16 回顾渲染方程、BRDF、BVH / KD 树、Path Tracing、Russian Roulette、Ray Reconstruction。
   - 与 P6 高级渲染形成考试 / 工业复习承接。

## 2. Source 对齐与缺口

| 项目 | Stage 1 结论 | 指南处理 |
|------|--------------|----------|
| Week15 课堂笔记 | 存在，ready | 作为 P7 收束、Alpha、VR、AI 趋势 raw |
| Week16 课堂记录 | 已由邮件课程总结脱敏导入，ready | 作为 P7 总复习、曲线曲面、管线、GPU-driven、光追 raw |
| Project 综合说明 | 缺失；只有前序作业和 Week16 复习提醒 | 不虚构 final project checklist，只写“作业/PPT 复习与项目整合思路” |
| 展示要求 | 缺失 | 不编写演示流程、PPT 时长或评分项 |
| 详细 rubric | 缺失；只有课程总成绩组成和作业过程导向等零散信息 | 不写具体评分表 |
| 期末范围 / 题型 | 部分存在：PPT 与作业内容、Alpha、Pipeline、Blinn-Phong、MVP、Shader 等；题型缺失 | 明确可确认考点与不可推断题型 |

## 3. 偏差审计

`source-boundary-week16-project-rubric` 仍在中段把“Part 7”误解为课件 `Lecture #7: Local Shading`，列出局部着色范围。该段与本任务定义的 **P7 = Week15-16 / 项目整合 / 展示 / 总复习** 不一致。

处理原则：

- 不把 `Lecture #7: Local Shading` 当成本 Part 主线。
- Blinn-Phong 因 Week16 明确列为考试重点，可进入总复习地图，但作为 P4 / 作业复习点，而不是 Week15-16 新授主线。
- Project / 展示 / rubric 缺失审计保留。

## 4. Stage 2 问题草案

1. `concept-breakdown-exam-homework-boundary`：展开期末范围、PPT / 作业关系、可确认与不可推断内容。
2. `concept-breakdown-alpha-color-display`：展开 Alpha 混合、颜色科学、HDR 和显示增强。
3. `concept-breakdown-curves-surfaces`：展开参数曲线 / 曲面、Bezier、B-spline、NURBS、连续性和 CAD 难点。
4. `concept-breakdown-pipeline-programmable-api`：展开渲染管线、MVP、齐次坐标、Shader、Buffer / descriptor binding。
5. `concept-breakdown-gpu-driven-rendering`：展开 Mesh Shader、Meshlet、Visibility Buffer、CPU-GPU 瓶颈和工业资料。
6. `concept-breakdown-vr-spatial-intelligence`：展开 VR / AR、分布式渲染、空间智能、高保真仿真和 AI 工具趋势。
7. `concept-breakdown-raytracing-review`：展开光线追踪、路径追踪、Ray Reconstruction 与 P6 复习承接。
