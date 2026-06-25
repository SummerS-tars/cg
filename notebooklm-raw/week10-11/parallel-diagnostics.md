# Week 10-11 / Part 5 Parallel Raw Diagnostics

> **记录时间**：2026-06-26  
> **实验范围**：P5 `week10-11` stage-1 与 P6 `week12-14` stage-1 两个 Part 同时采集 raw。  
> **P5 manifest**：`notebooklm-raw/manifests/week10-11-stage1.json`  
> **P5 run**：`notebooklm-raw/week10-11/runs/20260626-000200`

## 1. 结果

| 指标 | 结果 |
|------|------|
| 并行对象 | P6 `week12-14` stage-1 |
| P5 batch 数 | 4 |
| P5 completed | 4/4 |
| P5 failed | 0 |
| P5 retry | 0 |
| P5 总耗时 | 211.99s |
| 远端错误 | 未见 429、认证失败、超时或会话冲突 |
| 是否降级串行 | 否 |

## 2. 观察

- P5 第一次采集在 batch 1 提问阶段被用户中断，未生成 answer；后续使用 `--resume notebooklm-raw/week10-11/runs/20260626-000200` 继续，最终 run 正常 completed。
- P5 与 P6 使用不同 manifest、不同 module、不同 run directory，raw 文件未混写。
- 两个进程都使用 `clear_conversation: true`。本次未观察到回答串话，但这是后续并行时需要持续关注的风险点。

## 3. 判定

本次小并发对 P5 stage-1 可接受。后续若继续并行，应限制为两个 Part、每个 Part 内 stage 顺序不交叉，并在出现以下情况时立即回退串行：

- NotebookLM 返回 429、限流、连续连接失败或超时。
- `notebooklm clear` / `ask` 期间出现会话状态异常。
- batch answer 明显混入另一个 Part 的 prompt 或上下文。
- 同一 Part 的 stage 依赖产物尚未生成，例如未写 `stage1-summary.md` 就启动 stage-2。
