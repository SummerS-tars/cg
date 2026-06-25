# Week 3-4 / Part 2 Stage 1 Summary

> **生成时间**：2026-06-25  
> **输入 run**：`notebooklm-raw/week3-4/runs/20260625-223828`  
> **Stage 1 batches**：`overview-skeleton`、`slide-skeleton-lecture03`、`slide-skeleton-lecture04`  
> **认证 / source 校准**：WSL 初始认证失效；按 SOP 从 Windows storage `sync-auth --force` 后恢复。CG Notebook source list 共 29 个 ready source；Week 4 课件真实名称为 `课件04-Lecture04-05-2025`。

## 1. Stage 1 采集结论

Stage 1 确认 Part 2 的课程骨架不是单纯“矩阵公式合集”，而是从**几何变换**进入**3D 渲染管线中坐标如何流动**：

1. **Lecture03 / Week 3：几何变换**
   - 变换导论：变换把对象坐标映射到新位置，用于实例化和在不同坐标系中定义对象。
   - 2D / 3D 基本变换：缩放、旋转、平移、错切；3D 旋转需要轴和角度，顺序不交换。
   - 齐次坐标与 4x4 矩阵：用统一矩阵表达平移、旋转、缩放、错切、投影等。
   - 矩阵组合与顺序：组合顺序决定最终效果，是后续 Model/View/Projection 的基础。
   - 层次结构 / scene graph：用父子矩阵链组织复杂对象。
2. **Lecture04 / Week 4：3D Rendering Pipeline 的观察与投影段**
   - 渲染管线总览：模型变换、光照、视图变换、投影变换、裁剪、视口变换、扫描转换。
   - 相机模型：针孔相机、eye position、view direction、up direction、FOV、view plane。
   - 观察变换：把世界坐标映射到相机坐标；通过 R/U/B 基向量和相机位置构造 view matrix。
   - 投影变换：平行 / 正交 / 斜投影与透视投影；透视投影用相似三角形和 4x4 矩阵表达。
   - 裁剪、NDC 与视口：投影后进入裁剪、透视除法、标准化屏幕坐标，再映射到像素。
   - 可编程管线：Lecture04-05 末尾涉及 DX10/11/12 等后续内容，Stage 2 只作为管线位置背景，不作为 Part 2 深挖主线。

## 2. 真实模块与重要性

| 模块 | 重要性 | Stage 1 依据 | Stage 2 展开方向 |
|------|--------|--------------|------------------|
| 2D/3D 几何变换 | 核心 | `slide-skeleton-lecture03`、`overview-skeleton` | 基本变换矩阵、几何直觉、输入输出坐标、典型例子 |
| 齐次坐标与 4x4 矩阵 | 核心 | `overview-skeleton`、`slide-skeleton-lecture03` | 为什么平移需要齐次坐标，w 的意义，点/向量区分 |
| 变换组合与顺序 | 核心 | `slide-skeleton-lecture03` | 左乘/右乘、局部/世界坐标，顺序错误的视觉结果 |
| 3D 旋转、欧拉角、万向节死锁 | 重要 | `slide-skeleton-lecture03` | 轴角、右手定则、欧拉角局限；四元数只作为了解 |
| 层次结构 / Scene Graph | 重要 | `overview-skeleton`、`slide-skeleton-lecture03` | 父子变换链、机器人/骨骼例子、矩阵栈 |
| 相机模型与观察变换 | 核心 | `slide-skeleton-lecture04`、`overview-skeleton` | R/U/B 基、look-at、view matrix 构造和求逆 |
| 投影分类与透视投影 | 核心 | `slide-skeleton-lecture04`、`overview-skeleton` | 正交 vs 透视、相似三角形、frustum、投影矩阵 |
| 裁剪空间、NDC 与视口 | 核心 | `overview-skeleton`、`slide-skeleton-lecture04` | clip space、透视除法、NDC、viewport mapping |
| 几何原语、网格、Z-buffer、可编程管线 | 了解/后续承接 | `overview-skeleton`、`slide-skeleton-lecture04` | 只用于说明 Part 2 在完整渲染管线中的位置 |

## 3. Source 对齐与偏差

- `课件03-Lecture03-2026` 对应 Week 3 几何变换，source 名称与 manifest 一致。
- `课件04-Lecture04-05-2025` 同时覆盖 Lecture04 和 Lecture05。Stage 1 回答已区分 Week 4 / Part 2 范围和后续延伸内容。
- `overview-skeleton` 混入了几何原语、Z-buffer、可编程 pipeline 等完整管线后段；它们有助于定位，但在 Part 2 指南中应压缩为承接背景，不能抢占变换 / 相机 / 投影主线。

## 4. Stage 2 问题草案

Stage 2 应按真实骨架展开，不提前固定问 misconceptions / project-bridge：

1. `concept-breakdown-geometric-transforms`：展开 2D/3D 基本变换、齐次坐标、4x4 矩阵、点/向量区别。
2. `concept-breakdown-composition-hierarchy`：展开矩阵顺序、局部/世界坐标、scene graph / hierarchy。
3. `concept-breakdown-camera-view`：展开相机参数、R/U/B 基向量、look-at、view matrix。
4. `concept-breakdown-projection`：展开正交/透视投影、相似三角形、frustum、投影矩阵直觉。
5. `concept-breakdown-clip-ndc-viewport`：展开裁剪空间、透视除法、NDC、viewport mapping。
6. `slide-module-detail-lecture04-part2`：仅依据 `课件04-Lecture04-05-2025` 细化 Week 4 / Part 2 的相机、投影、裁剪与视口原序。
