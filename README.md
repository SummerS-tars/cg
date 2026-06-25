# CG 课件梳理与学习指南

计算机图形学（Computer Graphics, CG）课程的课件结构梳理与 NotebookLM 辅助学习指南。

## 目录结构

```
├── guides/                    # 学习指南（定稿）
│   ├── CG课程-16周内容梳理.md   # 全课程知识脉络总览（待真实资料校准）
│   ├── CG-Week1-2-学习指南.md
│   ├── CG-Week3-4-学习指南.md
│   └── ...
├── notebooklm-raw/           # NotebookLM 采集原始数据
│   ├── semester-parts.md       # Part 分组、同步状态与流水线矩阵
│   ├── manifests/             # 采集 manifest（提问计划）
│   ├── week1-2/               # 按周模块采集结果
│   ├── week3-4/
│   └── ...
└── .cursor/                   # Cursor IDE 项目工作流
```

## 工作流

1. **课件结构分析**：NotebookLM 限定相关课件 → 提取课件原序模块、图形管线、图片/示例与重点
2. **分层 raw 采集**：设计 v4 manifest → 骨架、知识点拆分、深挖、示例、易混点、Project 串联 → `notebooklm-raw/`
3. **知识图谱**：通读 raw → 产出认知阶梯、坐标/管线关系与叙事承接
4. **叙事整合**：按图谱撰写学习指南，补全景节、Mermaid/ASCII 图、易混对比，并完成内部 Review 迭代
5. **定稿**：用户 Review → 更新进度索引

## 工作流入口

- Cursor Skill：`.cursor/skills/cg-course-notebooklm/SKILL.md`
- 全课程总览：`guides/CG课程-16周内容梳理.md`
- Part / 同步矩阵：`notebooklm-raw/semester-parts.md`
- 整合规范：`.cursor/skills/cg-course-notebooklm/docs/integration-guide.md`
- 公开写作规范：`guides/学习指南整合规范.md`

## 主题覆盖

按课程材料逐步补齐，例如几何变换、投影、光照模型、光栅化、纹理映射、曲线曲面、可见性、渲染管线与课程 Project。

## 许可

仅供个人学习参考。
