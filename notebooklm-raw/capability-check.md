# NotebookLM 能力检查记录

> **日期**：2026-06-25  
> **范围**：CG NotebookLM 学习资料流水线、系统级认证同步、NotebookLM CLI 只读能力  
> **原则**：不读取或记录 cookie/token；不执行正式采集；不清空远端会话；不增删改 NotebookLM source。

## 结论

当前 NotebookLM 能力链路可用到“认证同步 + Notebook 列表 + CG Notebook source list + Python API 极小 ask + P1 正式采集”阶段。CG Notebook 的完整 UUID 已确认：

```text
c46f03a0-be2e-4cbb-8172-24a3ee0fce88
```

CG Notebook `source list --json` 返回 29 个 source，全部为 `ready`。P1 / `week1-2` 已创建真实 manifest，完成 12 个 batch raw 采集，并生成 `knowledge-graph.md`、学习指南与内部 review 记录。

## 复用的 Windows 侧验证

复用依据来自本机既有诊断记录：`/home/thesumst/development/jizu/notebooklm-raw/kejian04/auth-diagnosis.md`。该记录说明：

- Windows 侧使用 `C:\Users\Sum\Desktop\notebooklm-login.ps1`，实际调用 `fix_login_edge.py`，将登录态保存到 `C:\Users\Sum\.notebooklm\storage_state.json`。
- WSL 侧使用系统级 `~/service/openclaw/workspace/skills/notebooklm-integration/scripts/sync-auth.py` 消费该 storage。
- 2026-06-24 已验证 `sync-auth.py --check`、计组 Notebook `use`、`source list --json` 与极简 `ask` 可用。

本次检查中，初始 `sync-auth.py --status` 显示 WSL 认证已失效，但 Windows storage 存在且较新，状态提示 `needs sync from Windows`。按上述 SOP 运行 `sync-auth.py --force` 后，WSL storage 与 Windows storage mtime 对齐，`sync-auth.py --check` 返回认证有效。

## 本次轻量验证

在仓库根目录 `/home/thesumst/development/cg` 执行：

```bash
python3 - <<'PY'
from pathlib import Path
p = Path('.cursor/skills/cg-course-notebooklm/scripts/nlm-collect.py')
compile(p.read_text(encoding='utf-8'), str(p), 'exec')
print('compile OK:', p)
PY
```

结果：`nlm-collect.py` 语法编译通过。

```bash
python3 .cursor/skills/cg-course-notebooklm/scripts/nlm-collect.py --help
```

结果：帮助信息正常显示，支持 `--dry-run`、`--resume`、`--only`、`--no-auth`、`--proxy`、`merge-runs` 等入口。

```bash
python3 .cursor/skills/cg-course-notebooklm/scripts/nlm-collect.py \
  .cursor/skills/cg-course-notebooklm/templates/manifest-template.json \
  --dry-run
```

结果：dry-run 正常解析 5 个 batch，不调用 NotebookLM API，不写入 run。

```bash
python3 ~/service/openclaw/workspace/skills/notebooklm-integration/scripts/sync-auth.py --force
python3 ~/service/openclaw/workspace/skills/notebooklm-integration/scripts/sync-auth.py --status
python3 ~/service/openclaw/workspace/skills/notebooklm-integration/scripts/sync-auth.py --check
```

结果：Windows storage 成功同步到 WSL，`auth: valid`，认证检查通过。

```bash
export HTTPS_PROXY=http://127.0.0.1:7897 HTTP_PROXY=http://127.0.0.1:7897
~/service/openclaw/workspace/skills/notebooklm-integration/.venv/bin/notebooklm list --json
```

结果：代理环境下成功返回 13 个 Notebook，其中包含 `计算机图形学 Notebook`。

```bash
~/service/openclaw/workspace/skills/notebooklm-integration/.venv/bin/notebooklm \
  use c46f03a0-be2e-4cbb-8172-24a3ee0fce88
~/service/openclaw/workspace/skills/notebooklm-integration/.venv/bin/notebooklm \
  source list --json
```

结果：CG Notebook 可选中；source list 返回 29 个 source，全部 `ready`。

## CG Notebook source 概况

已确认 source 类型：

- 课堂笔记：`笔记-week01-周一-图形学`、`笔记-week02-周一-图形学`、`笔记-week03-周一-图形学`、`笔记-week04-周一-图形学`、`笔记-week05-周一-图形学`、`笔记-week07-周一-图形学`、`笔记-week08-周一-图形学`、`笔记-week09-周一-图形学`、`笔记-week11-周一-图形学`、`笔记-week12-周一-图形学`、`笔记-week13-周一-图形学`、`笔记-week14-周一-图形学`、`笔记-week15-周一-图形学`。
- 课件 PDF：`课件01-Lecture01-2026` 至 `课件09-Lecture11-part2-路径追踪-2026`。
- 论文/补充材料：Brook for GPUs、GPU-Driven Rendering Pipelines、Improved Illumination Model、OptiX、Particle Transport and Image Synthesis、Ray Tracing in One Weekend、The Rendering Equation。

## 当前可用能力

- Windows 登录态可通过 `sync-auth.py --force` 同步到 WSL。
- `sync-auth.py --check` 可验证 token fetch。
- NotebookLM CLI 在设置 `HTTP_PROXY`、`HTTPS_PROXY`、`http_proxy`、`https_proxy` 为 `http://127.0.0.1:7897` 后可列出 Notebook。
- `notebooklm-py 0.3.4` Python API 已验证：`AuthTokens.from_storage()` 可读取 cookies 并 fetch csrf/session token，`NotebookLMClient(auth, timeout=...)` 可 ask，返回正文为 `AskResult.answer`。
- CG Notebook 的完整 UUID 与 source list 已确认。
- `nlm-collect.py` 可解析 manifest、dry-run、续跑与补采参数，并会为 `sync-auth`、NotebookLM CLI、Python API 同步注入大小写代理变量。

## 当前不可用或未验证能力

- P1 正式 `nlm-collect.py` 采集已完成；后续 Part 尚未创建 manifest。
- CG Notebook 极简 `ask` 已运行，返回 `CG Notebook API 探测 OK。`。
- 未确认 Week 6/10/16 是否因停课、资料缺失或 source 命名差异而不存在。
- 未确认 Project、作业、评分标准等 source 是否已上传到 CG Notebook。

## 下一步

1. 用户 Review `guides/CG-Week1-2-学习指南.md`，确认是否需要补采 Project/作业细则或 Bresenham 完整数值例。
2. 用户确认 Week 6/10/16 的课程状态，以及 Project/作业资料是否已上传或需从本地补齐。
3. 继续以 `c46f03a0-be2e-4cbb-8172-24a3ee0fce88` 为后续 Part 创建 v4 manifest，再进入分 Part 深采。

## 2026-06-25 代理与 v0.3.4 API 复查

用户指出此前 Part 1 端到端试跑失败可能由缺少代理与 `notebooklm-py 0.3.4` API 变更导致。复查结论：

- 本地环境 `printenv` 未发现 `HTTP_PROXY` / `HTTPS_PROXY` / `http_proxy` / `https_proxy`。
- 项目根目录不存在 `.openclaw/.env`，本次未擅自创建项目配置目录；改由采集脚本和文档显式设置代理。
- 本地包为 `notebooklm-py 0.3.4`，`NotebookLMClient` 签名为 `NotebookLMClient(auth: AuthTokens, timeout=30.0)`，`AuthTokens` 需要 `cookies`、`csrf_token`、`session_id`。
- `AuthTokens.from_storage()` 会读取 storage cookies 并异步 fetch `csrf_token` / `session_id`；脚本已改为显式构造 auth 后再创建 client。
- `ChatAPI.ask()` 返回 `AskResult(answer=...)`；脚本读取 `answer`，并保留旧字段 `text` fallback。
- 极小 ask 探测成功，返回 `CG Notebook API 探测 OK。`。
- P1 续跑成功：`notebooklm-raw/week1-2/runs/20260625-213138`，12/12 ok，0 retry，状态 completed。
