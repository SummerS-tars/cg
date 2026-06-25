# Part 2 / Week 3-4 Stage 1 采集诊断

> **日期**：2026-06-25  
> **阶段**：v4.1 dynamic raw `stage-1-skeleton`  
> **目标 manifest**：`notebooklm-raw/manifests/week3-4-stage1.json`

## 采集范围

Part 2 依据 `notebooklm-raw/semester-parts.md` 与 `guides/CG课程-16周内容梳理.md` 定义为 Week 3-4：变换、坐标系、相机 / 观察变换、正交与透视投影、裁剪空间与 NDC。

## 已完成

- 已生成 stage-1 manifest：`notebooklm-raw/manifests/week3-4-stage1.json`。
- stage-1 仅包含骨架类 batch：`overview-skeleton`、`slide-skeleton-lecture03`、`slide-skeleton-lecture04`。
- manifest 已明确正式 batch 使用 `clear_conversation: true`，并要求 stage-1 raw 由 Agent 摘要后显式写入 stage-2 manifest。

## 失败诊断

尝试列出 NotebookLM source 时出现：

```text
Server disconnected without sending a response.
```

随后执行认证检查：

```text
认证已失效（token fetch 失败）
```

尝试非登录同步认证路径后仍失败，输出提示：

```text
[WARN] 认证已失效（token fetch 失败）
[OK] 已同步: /home/thesumst/.notebooklm/storage_state.json

请在 Windows 重新登录（用户手动，Agent 勿从 WSL 触发）：
  桌面: C:\Users\Sum\Desktop\notebooklm-login.ps1
  或 PowerShell:
    cd E:\_WSL\Cowork\notebooklm-py_Prepare
    .\venv\Scripts\Activate.ps1
    python fix_login_edge.py

登录完成后在 WSL 运行: python3 scripts/sync-auth.py --force
```

## 处理决定

根据 CG NotebookLM workflow 约束，Agent 不在 WSL 执行 `notebooklm login`、不触发浏览器登录，也不伪造 raw。Part 2 raw 采集停止在 stage-1 manifest 生成后，等待用户在 Windows 侧重新登录并同步认证。

## 恢复步骤

1. 用户在 Windows 侧重新登录 NotebookLM。
2. 在 WSL 同步认证后，先校准 source list。
3. 运行：

```bash
NLM=.cursor/skills/cg-course-notebooklm/scripts/nlm-collect.py
python3 "$NLM" notebooklm-raw/manifests/week3-4-stage1.json --dry-run
python3 "$NLM" notebooklm-raw/manifests/week3-4-stage1.json --delay 8
```

4. 通读 stage-1 answers，生成 `notebooklm-raw/week3-4/stage1-summary.md` 和 `week3-4-stage2.json`。
