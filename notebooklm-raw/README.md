# NotebookLM 原始采集区

本目录存放计算机图形学课程的 NotebookLM 原始采集结果。详细策略见：

`.cursor/skills/cg-course-notebooklm/docs/raw-data.md`

**工作流入口**：`.cursor/skills/cg-course-notebooklm/SKILL.md`

**NotebookLM 认证 SOP**：`~/service/openclaw/workspace/skills/notebooklm-integration/docs/auth-sop.md`

## 约定

- `manifests/`：采集计划，每个 manifest 对应一个周次或模块。
- `<module>/runs/latest/`：最近完成的一轮采集。
- `<module>/knowledge-graph.md`：通读 raw 后产出的知识图谱，必须先于学习指南正文。
- `*.answer.md`：Agent 整合学习指南时使用的主要素材。
