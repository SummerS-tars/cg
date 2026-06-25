# Week 5-6 / Part 3 Stage 1 Summary

> **生成时间**：2026-06-25  
> **输入 run**：`notebooklm-raw/week5-6/runs/20260625-232348`  
> **Stage 1 batches**：`overview-skeleton`、`slide-skeleton-lecture04-05-part3`、`slide-skeleton-lecture06`  
> **认证 / source 校准**：`sync-auth --check` 可用；CG Notebook source list 共 29 个 ready source。P3 可见 source 包括 `笔记-week05-周一-图形学`、`课件04-Lecture04-05-2025`、`课件05-Lecture06-2025`；未发现 Week 6 课堂笔记或 Project / Assignment 文档。

## 1. Stage 1 采集结论

Stage 1 确认 Part 3 的真实材料不是完整覆盖“光栅化 / 可见性 / 采样”的三件套，而是从 Part 2 的相机投影继续进入**3D Rendering Pipeline 后段、Clipping、Viewport Transformation、Scan Conversion、Programmable Pipeline 与 Hidden Surface Removal**：

1. **Lecture04-05 后半：渲染管线后段**
   - 裁剪(Clipping)：投影后、视口前，丢弃视量体 / 窗口外的几何部分。
   - 视口变换(Viewport Transformation)：把规范化窗口 / NDC 位置映射到实际屏幕或图像坐标。
   - 扫描转换(Scan Conversion)：把几何原语转换为像素 / 片元，是输出图像前的关键阶段。
   - 固定管线到可编程管线(Programmable Pipeline)：DX10/11/12 等示意图展示现代 GPU 管线和 shader 阶段。
2. **Lecture06：Hidden Surface Removal**
   - 消隐(Hidden Surface Removal, HSR)：判断表面可见或被遮挡。
   - 管线位置：几何变换、投影和裁剪之后，扫描转换之前或期间。
   - 分类：物体空间(Object Space)算法与图像空间(Image Space)算法。
   - 重点算法：Back-face Culling、Depth Sort / Painter、Ray Casting、Z-buffer、A-buffer、Scan-line、Area Subdivision、BSP Tree。
3. **Week 5 课堂记录的工程承接**
   - Week 5 笔记提到现代 API / Vulkan、GPU 资源管理、shader 中手动矩阵计算等工程任务。
   - 这些内容应作为“管线架构与工程位置”处理，不抢占 P3 的可见性与光栅化主线。

## 2. 真实模块与重要性

| 模块 | 重要性 | Stage 1 依据 | Stage 2 展开方向 |
|------|--------|--------------|------------------|
| 3D Rendering Pipeline 后段 | 核心 | `overview-skeleton`、`slide-skeleton-lecture04-05-part3` | 从 Projection 后接到 Clipping、Viewport、Scan Conversion、HSR，解释每步输入输出 |
| Clipping 与 Viewport Transformation | 重要 | `overview-skeleton`、`slide-skeleton-lecture04-05-part3` | Cohen-Sutherland、Liang-Barsky、window-to-viewport 映射；承接 Part 2 的 Clip/NDC |
| Scan Conversion / Rasterization 位置 | 核心但 raw 较薄 | `slide-skeleton-lecture04-05-part3` | 解释几何到像素的角色；若 NotebookLM 只给概念层，指南中需谨慎补 Agent 直观，不伪造课件细节 |
| Programmable Pipeline | 重要 | `overview-skeleton`、`slide-skeleton-lecture04-05-part3`、Week 5 笔记 | 固定管线到 shader；说明 MVP / clipping / rasterization 在现代 API 中的工程位置 |
| Hidden Surface Removal 总览 | 核心 | `overview-skeleton`、`slide-skeleton-lecture06` | 消隐问题、背面/遮挡/重叠、object-space vs image-space |
| Z-buffer、A-buffer 与 Ray Casting | 核心 | `slide-skeleton-lecture06` | 深度缓冲、可见性判断、与扫描转换 / fragment 的关系 |
| BSP Tree、Scan-line、Area Subdivision | 了解/重要 | `slide-skeleton-lecture06` | 作为可见性算法族对比，重点放原理与适用位置 |
| Sampling / Anti-aliasing | 缺口 | `semester-parts.md` 与 16 周框架预期；Stage 1 raw 未实质覆盖 | 不作为 stage-2 主线展开；在 focus map 中记录是否需要后续补采或标为资料缺失 |

## 3. Source 对齐与偏差

- `笔记-week05-周一-图形学` 存在，并混合了 pipeline、Vulkan、shader 工程任务与消隐前后承接。
- 未发现 `笔记-week06-CG` / `笔记-week06-周一-图形学`，因此 Week 6 具体课堂顺序无法由 raw 验证。
- 未发现 Project / Assignment 文档；Week 5 笔记里有工程任务线索，但不能当作正式 Project 文档。
- `课件04-Lecture04-05-2025` 后半进入 P3 范围；其前半相机 / 投影内容应作为 Part 2 承接压缩处理。
- `课件05-Lecture06-2025` 明确对应 Hidden Surface Removal，是 P3 的核心课件。
- `semester-parts.md` 预期的“采样 / 抗锯齿”在 Stage 1 raw 中缺少明确 source；后续指南必须说明资料缺口，不能伪造 raw。

## 4. Stage 2 问题草案

Stage 2 应围绕真实骨架展开，不提前固定 `misconceptions-*` 或 `project-bridge`：

1. `concept-breakdown-pipeline-after-projection`：展开投影后到像素前的管线后段，串联 Part 2。
2. `concept-breakdown-clipping-viewport`：展开 clipping、Cohen-Sutherland、Liang-Barsky、viewport mapping。
3. `concept-breakdown-scan-conversion-rasterization`：展开 scan conversion / rasterization 的角色、输入输出与像素化直觉。
4. `concept-breakdown-programmable-pipeline`：展开 fixed pipeline 到 programmable pipeline、shader 阶段和现代 API 位置。
5. `concept-breakdown-hidden-surface-overview`：展开 HSR 问题、分类、背面剔除、画家算法。
6. `concept-breakdown-depth-buffer-algorithms`：展开 Z-buffer、A-buffer、Ray Casting、BSP / scan-line / area subdivision 的关系。
