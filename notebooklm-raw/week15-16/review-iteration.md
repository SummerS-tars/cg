# Week 15-16 / Part 7 Review Iteration

## 内部 Review 1：资料边界

- 检查结果：Week16 课程总结已从本地 FiCS/iCourse 导出、脱敏并加入 NotebookLM，状态 ready。
- 处理：P7 范围更新为 Week15 + Week16；不再标注 Week16 缺失。
- 仍缺失：Project 展示要求、详细 rubric、考试题型与分值分布。

## 内部 Review 2：NotebookLM 偏差

- 检查结果：`source-boundary-week16-project-rubric` 把“Part 7”误解为 Lecture 7 Local Shading。
- 处理：指南不把 Local Shading 当 P7 主线；Blinn-Phong 只作为 Week16 明确提到的作业 / P4 复习点。

## 内部 Review 3：公式与例题

- Alpha raw 中 $\alpha$ 范围曾被引用编号污染为 `$[4]` 或 `$[0]` 类似形式。
- 处理：最终指南统一修正为 $\alpha\in[0,1]$，并给出普通混合与投影融合两个例子。

## 内部 Review 4：术语与英语考试格式

- 检查术语：Image Compositing、Alpha Blending、MVP、Shader、Buffer、Descriptor Set、NURBS、GPU-driven Rendering、Mesh Shader、Visibility Buffer、VR、AIGC、Sim-to-Real。
- 处理：术语表和正文首次出现使用 `中文(English)` 或 `Abbr(Full English Name，中文对照)`，重点缩写均解释。

## 内部 Review 5：最终整合检查

- 每个主体章节就近放 `参考 raw`。
- Mermaid 图包含资料边界、Alpha 投影融合、渲染管线、VR / AI 收束链路。
- 表格避免竖线数学表达；数学公式使用 LaTeX。
- 最终指南不包含采集计划、补采计划或操作步骤。
- Project / rubric 缺失只作为资料边界说明，不虚构 checklist。
