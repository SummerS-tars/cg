# Week 12-14 / Part 6 Parallel Raw Diagnostics

> **记录时间**：2026-06-26  
> **实验范围**：P6 `week12-14` stage-1 与 P5 `week10-11` stage-1 两个 Part 同时采集 raw。  
> **P6 manifest**：`notebooklm-raw/manifests/week12-14-stage1.json`  
> **P6 run**：`notebooklm-raw/week12-14/runs/20260626-000323`

## 1. 结果

| 指标 | 结果 |
|------|------|
| 并行对象 | P5 `week10-11` stage-1 |
| P6 batch 数 | 5 |
| P6 completed | 5/5 |
| P6 failed | 0 |
| P6 retry | 0 |
| P6 总耗时 | 278.69s |
| 远端错误 | 未见 429、认证失败、超时或会话冲突 |
| 是否降级串行 | 否 |

## 2. 观察

- P6 使用独立 run directory：`notebooklm-raw/week12-14/runs/20260626-000323`。
- 与 P5 同时运行时，P6 各 batch 平均耗时约 39-56s，未出现重试。
- 两个进程的 batch 边界在时间上有交叠，说明 NotebookLM 当前环境可承受两个 Part 的 stage-1 小并发。

## 3. 判定

本次小并发对 P6 stage-1 可接受。后续并行策略应保持：

- 最多两个 Part 同时 raw 采集。
- 同一 Part 内保持 `stage-1 -> stage1-summary -> stage-2 -> focus-map -> stage-3` 顺序。
- 每个 Part 保持独立 manifest、run directory、summary、focus map 和 diagnostics。
- 一旦出现限流、认证、超时、连续连接失败或答案混线，立即停止并回退串行。
