# 采集与整合排错

> **认证权威 SOP**：`~/service/openclaw/workspace/skills/notebooklm-integration/docs/auth-sop.md`

## RPC GET_NOTEBOOK / null result（短 Notebook ID）

**现象**：`RPC rLM1Ne returned null result data`，`GET_NOTEBOOK failed`；CLI `notebooklm ask` 正常但 `nlm-collect.py` 失败。

**原因**：manifest 里用了短前缀；`notebooklm-py` 的 `chat.ask()` 需要**完整 UUID**。

**处理**：
1. `notebooklm list` 查完整 ID
2. 更新 manifest 中的 `notebook_id` 为完整 UUID
3. 当前 CG Notebook：首次采集前由用户确认并写入 manifest

## 认证失败

**现象**：`Authentication expired or invalid`，或 sync-auth 失败。

**处理（唯一正确流程）**：
1. **用户**在 Windows 运行桌面 `notebooklm-login.ps1`，或 `fix_login_edge.py`（见 auth-sop.md）
2. WSL：
   ```bash
   python3 ~/service/openclaw/workspace/skills/notebooklm-integration/scripts/sync-auth.py --force
   python3 ~/service/openclaw/workspace/skills/notebooklm-integration/scripts/sync-auth.py --check
   ```

**Agent 禁止**：`notebooklm login`、WSL 浏览器登录、从 WSL 触发 Windows Edge、`sync-auth --refresh`（已废弃）。

CLI 报 `Run 'notebooklm login'` 时忽略，改走 Windows + sync-auth。

## 超时（~32s）

**现象**：`Chat request timed out`，elapsed ≈ 30–35s。

**原因**：notebooklm-py 默认 HTTP 读超时 30s；成功回答常需 40–50s。

**处理**：
- 脚本已默认 `--nlm-timeout 120`、`--retries 3`
- 加大间隔：`--delay 8`
- 续跑：`--resume notebooklm-raw/<module>/runs/latest`

## 部分 batch 失败

- 默认继续跑完其余 batch（不加 `--fail-fast`）
- 查看 `run.log` 与 `run.meta.json` 的 `error_kind`
- 补采：`--only <batch> --resume runs/latest`
- 或 `merge-runs <补采run> runs/latest`

## 代理

WSL 访问 Google / `notebooklm.google.com` 必须 `http://127.0.0.1:7897`。同时设置大小写变量，避免 CLI 与 `notebooklm-py/httpx` 行为不一致：

```bash
export HTTPS_PROXY=http://127.0.0.1:7897 HTTP_PROXY=http://127.0.0.1:7897
export https_proxy=http://127.0.0.1:7897 http_proxy=http://127.0.0.1:7897
```

`nlm-collect.py` 已默认把四个变量传给 `sync-auth`、NotebookLM CLI 和 Python API。若日志中每次 `ask` 都在约 30s 后空错误/超时，优先检查代理变量是否进入 Python 进程。

## notebooklm-py v0.3.4 API 适配

- `NotebookLMClient()` 不能无参构造；脚本使用 `AuthTokens.from_storage()` 读取 cookies，并异步 fetch `csrf_token` / `session_id` 后构造 `NotebookLMClient(auth, timeout=...)`。
- `ask` 返回正文是 `AskResult.answer`；脚本保留旧字段 `text` fallback，落盘仍统一写入 `answer`。

## 整合质量

| 症状 | 对策 |
|------|------|
| 公式堆砌、无全景 | 补 Phase 1.5 知识图谱 + 全景节 |
| 坐标/矩阵不直观 | 补几何意义、管线位置、输入输出和小例子 |
| 语言生硬 | 按 `integration-guide.md` 加视觉类比、追问块 |
| NotebookLM 与课纲不符 | 以课堂记录/课件为准，指南中标注 |
