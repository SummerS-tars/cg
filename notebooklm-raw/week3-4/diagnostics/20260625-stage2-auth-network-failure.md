# Part 2 / Week 3-4 Stage 2 采集诊断

> **日期**：2026-06-25  
> **阶段**：v4.1 dynamic raw `stage-2-module-expansion`  
> **目标 manifest**：`notebooklm-raw/manifests/week3-4-stage2.json`  
> **Stage 2 run**：`notebooklm-raw/week3-4/runs/20260625-224204`

## 认证与代理检查

按 NotebookLM SOP 设置代理：

```bash
HTTP_PROXY=http://127.0.0.1:7897
HTTPS_PROXY=http://127.0.0.1:7897
http_proxy=http://127.0.0.1:7897
https_proxy=http://127.0.0.1:7897
```

本轮开始前执行过安全恢复：

1. 初始 `sync-auth.py --status` 显示 WSL 认证失效，Windows storage 存在且较新。
2. 执行 `sync-auth.py --force` 从 Windows storage 同步到 WSL。
3. `sync-auth.py --check` 一度通过，`notebooklm list --json` 和 CG Notebook `source list --json` 通过；source list 共 29 个 ready source。
4. 确认 Week 4 课件真实名称为 `课件04-Lecture04-05-2025`，并已校准 stage-1 manifest。

## 已完成 raw

Stage 1 run `notebooklm-raw/week3-4/runs/20260625-223828` 已完成：

- `overview-skeleton`：ok
- `slide-skeleton-lecture03`：ok
- `slide-skeleton-lecture04`：ok

Stage 2 run `notebooklm-raw/week3-4/runs/20260625-224204` 部分完成：

- `concept-breakdown-geometric-transforms`：ok
- `concept-breakdown-composition-hierarchy`：ok
- `concept-breakdown-camera-view`：ok
- `concept-breakdown-projection`：ok
- `concept-breakdown-clip-ndc-viewport`：failed
- `slide-module-detail-lecture04-part2`：failed

## 失败现象

首次 stage-2 运行在第 5 个 batch 附近被中断前，日志出现：

```text
[SSL: RECORD_LAYER_FAILURE] record layer failure
Chat request failed: Server disconnected without sending a response.
```

续跑同一 run 时，第 5 / 6 个 batch 仍失败：

```text
[SSL: RECORD_LAYER_FAILURE] record layer failure
Chat request failed: peer closed connection without sending complete message body (incomplete chunked read)
Connection failed calling GET_NOTEBOOK
Chat request failed: Server disconnected without sending a response.
```

随后重新检查认证：

```text
sync-auth.py --check
认证已失效（token fetch 失败）
```

再次按安全路径执行 `sync-auth.py --status && sync-auth.py --force && sync-auth.py --check` 时，`--status` 一度显示 `auth: valid`，但同步后的 `--check` 又返回：

```text
认证已失效（token fetch 失败）
```

## 处理决定

根据 CG NotebookLM workflow 与 auth SOP：

- 不在 WSL 执行 `notebooklm login`。
- 不从 WSL 触发 Windows 浏览器登录。
- 不伪造 raw、不用已有 partial raw 假装完成 Stage 2/3。

因此 Part 2 当前停止在：

1. stage-1 完成；
2. `stage1-summary.md` 完成；
3. stage-2 manifest 完成；
4. stage-2 真实 raw 完成 4/6，剩余 2 个 batch 因认证 / 网络状态不稳定失败。

## 恢复步骤

用户需要在 Windows 侧重新刷新 NotebookLM 登录态：

```powershell
C:\Users\Sum\Desktop\notebooklm-login.ps1
```

或：

```powershell
cd E:\_WSL\Cowork\notebooklm-py_Prepare
.\venv\Scripts\Activate.ps1
python fix_login_edge.py
```

Windows 输出 `OK: saved ...` 后，在 WSL 运行：

```bash
cd ~/service/openclaw/workspace/skills/notebooklm-integration
source .venv/bin/activate
export HTTPS_PROXY=http://127.0.0.1:7897 HTTP_PROXY=http://127.0.0.1:7897
export https_proxy=http://127.0.0.1:7897 http_proxy=http://127.0.0.1:7897
python3 scripts/sync-auth.py --force
python3 scripts/sync-auth.py --check
```

认证恢复后续跑：

```bash
cd /home/thesumst/development/cg
python3 .cursor/skills/cg-course-notebooklm/scripts/nlm-collect.py \
  notebooklm-raw/manifests/week3-4-stage2.json \
  --resume notebooklm-raw/week3-4/runs/20260625-224204 \
  --only concept-breakdown-clip-ndc-viewport,slide-module-detail-lecture04-part2 \
  --delay 8
```
