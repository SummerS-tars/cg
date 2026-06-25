# NotebookLM 能力检查记录

> **日期**：2026-06-25  
> **范围**：CG NotebookLM 学习资料流水线、系统级认证同步、NotebookLM CLI 只读能力  
> **原则**：不读取或记录 cookie/token；不执行正式采集；不清空远端会话；不增删改 NotebookLM source。

## 结论

当前 NotebookLM 能力链路可用到“认证同步 + Notebook 列表 + CG Notebook source list + 本地采集脚本 dry-run”阶段。CG Notebook 的完整 UUID 已确认：

```text
c46f03a0-be2e-4cbb-8172-24a3ee0fce88
```

CG Notebook `source list --json` 返回 29 个 source，全部为 `ready`。仓库仍未创建真实采集 manifest，也没有 `notebooklm-raw/<module>/runs/latest/*.answer.md`，因此还不能进入知识图谱或学习指南定稿阶段。

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
- NotebookLM CLI 在设置 `HTTP_PROXY/HTTPS_PROXY=http://127.0.0.1:7897` 后可列出 Notebook。
- CG Notebook 的完整 UUID 与 source list 已确认。
- `nlm-collect.py` 可解析 manifest、dry-run、续跑与补采参数。

## 当前不可用或未验证能力

- 未运行正式 `nlm-collect.py` 采集，因为当前仓库尚无真实 CG manifest，且模板 batch 会 `clear_conversation`，不适合作为能力检查直接执行。
- 未运行 CG Notebook 极简 `ask`，避免在未确认前向远端 Notebook 写入新对话；如用户确认，可用单问短 prompt 做最终 chat/API 探测。
- 未确认 Week 6/10/16 是否因停课、资料缺失或 source 命名差异而不存在。
- 未确认 Project、作业、评分标准等 source 是否已上传到 CG Notebook。

## 下一步

1. 用户确认是否允许对 CG Notebook 运行一次极简 `ask`，例如“请只回答：CG Notebook 能力检查 OK。”。
2. 用户确认 Week 6/10/16 的课程状态，以及 Project/作业资料是否已上传或需从本地补齐。
3. 以 `c46f03a0-be2e-4cbb-8172-24a3ee0fce88` 创建第一份真实 manifest，建议先做 P1/P2 的 L0 discovery，再进入分 Part 深采。
