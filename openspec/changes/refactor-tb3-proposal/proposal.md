# TB3 Proposal Refactor and Navigation Mission Plan

## Why

原提案描述了任務流程，但敘述式設計尚未形成逐項可驗收的行為規格。DIC3 將既有離線功能建立為 baseline，並將中文任務、導航監控與評估轉成待實作規格，讓文件、程式與測試能逐項核對。

## What Changes

- 重寫 PROPOSAL.md 的 A–F 摘要、Introduction 與 Related Work，保留原本五核心、三取捨、十個問題。
- 建立既有 offline-contract baseline，以及下列兩項新能力的規格與驗收情境。
- 將根目錄 DESIGN.md 對應到 OpenSpec proposal、design、specs、tasks；補上取消、終點驗證與重試界線。
- 提供 DIC3 導覽、重現指令及真實驗證紀錄。本次修改完成提案與規格；LLM／ROS 整合仍待實作。

## Capabilities

### New Capabilities

- `navigation-mission`: 中文任務澄清、受限地點派送、狀態檢查、監控、有限重試與可追溯回報。
- `mission-evaluation`: 固定條件的比較、資料切分、指標與模擬／實機來源區分。

### Modified Capabilities

無。offline-contract 為既有程式的補建基準，這次不改變其執行行為。

## Impact

新增 OpenSpec 與 DIC3 文件；更新提案文字及 README／DESIGN 導覽。src、tests、Dockerfile 不變；既有 PDF／PPTX 保留為期中版本。OpenSpec 是文件開發工具，不加入機器人 runtime。正式導航 API、ROS 發行版、模型及各項門檻須在後續整合前確認。
