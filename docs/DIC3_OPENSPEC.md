# DIC3：使用 OpenSpec 重整 TB3 專題提案

日期：2026-11-12  
整理：蕭丞皓（7115064186）  
專題：TurtleBot3 Burger 室內導航與任務決策 AI Agent

## 一、作業內容與檔案對照

| 教師要求 | 本專案內容 | 檔案 |
|---|---|---|
| 安裝 OpenSpec、熟悉規格驅動開發 | OpenSpec 2.0.0 初始化、CLI 流程與實際驗證紀錄 | 本文件、DIC3_VALIDATION.md |
| A–F 摘要 | 動機、挑戰、解法、方法、評估、預期產出；另附中英文摘要 | ../PROPOSAL.md 第 1 節 |
| 5 cores | 定位不確定、感測限制、車身限制、分層控制、可重現評估 | ../PROPOSAL.md 第 4.1 節 |
| 3 trade-offs | 模組化與端對端、地圖與無地圖、保守距離與效率 | ../PROPOSAL.md 第 4.2 節 |
| 10 details | 十個深入理解問題，涵蓋機制、故障與評估判斷 | ../PROPOSAL.md 第 4.3 節 |
| DESIGN 轉 OpenSpec workflow | 動機、需求情境、設計決策、任務與驗收對照 | ../openspec/changes/refactor-tb3-proposal/ |
| Introduction refactor | 背景、問題、RQ1–RQ3、預期貢獻與範圍 | ../PROPOSAL.md 第 2 節 |
| Related Work refactor | 語言代理、可行性、導航、評估與本組研究缺口 | ../PROPOSAL.md 第 3 節 |

已核對教師範例中的 [期末專題提案作業規範文字擷取版](https://github.com/huanchen1107/2026-11-11-DIC3-ProjectRefactor/blob/main/myplan/期末專題提案作業規範-文字擷取.md) 第三節：五核心須說明意義、證據及對系統設計的影響；三個專業爭論須整理雙方觀點、證據、共識與未解問題；十個深入理解問題須涵蓋原因、假設情境、取捨、故障、證據或設計判斷。本版依此對應原提案 4.1、4.2、4.3。該檔註明是原 PDF 的文字擷取，版面及圖片仍以原附件為準。

教師範例目前主要包含 README、myplan 規畫紀錄及附件文字擷取，沒有 openspec/ 資料夾；DIC3 作業頁另要求安裝 OpenSpec 並轉換 DESIGN，因此本專案同時保留提案重整與 OpenSpec 工作流程。範例中的期末簡報／影片要求屬原期末專題交付，不能直接當成這次 DIC3 必須全部完成的新增工作。

## 二、規格驅動開發的實際用途

先寫清楚「遇到什麼輸入，系統必須做什麼」，再決定實作與驗收。以「去門口」為例：若有兩個符合的地點，規格要求先詢問，而且不能派送；後續測試就能檢查是否真的沒有送出導航 goal。

本專案將兩種狀態分開：

- `openspec/specs/offline-contract/spec.md`：現有 Python 範例的實際契約，只接收 JSON、只產生 mock 結果。
- `openspec/changes/refactor-tb3-proposal/specs/`：完整中文任務與評估的待實作規格。尚未經模擬或實機驗收，因此保留在 change 中。

## 三、文件流程與系統流程

OpenSpec 的開發流程：

1. `proposal.md`：為什麼改、要增加哪些能力。
2. `specs/*/spec.md`：系統應有的行為與 WHEN／THEN 驗收情境。
3. `design.md`：如何設計、採用哪些取捨、如何對應原 DESIGN。
4. `tasks.md`：完成項目與待辦項目。
5. 實作與驗收後更新勾選狀態，確認完成才 archive。

系統執行流程：中文輸入 → 歧義澄清與白名單驗證 → 狀態／路徑檢查 → 派送／監控 → 終點、取消或逾時確認 → 證據回報。兩種流程分別描述「如何開發」與「程式如何執行」。

## 四、安裝與重現

本次已在作業準備環境安裝 OpenSpec 2.0.0、執行 init，並將規格與設定納入專案。這不代表使用者電腦已安裝。若要在自己的 Ubuntu 重現，先在終端機檢查：

```bash
node --version
npm --version
```

官方 npm 安裝方式需要 Node.js 22.12.0 以上。本次固定版本以方便重現：

```bash
npm install -g @fission-ai/openspec@2.0.0
openspec --version
cd tb3-navigation-agent-dic3-refactor
```

檔案已經初始化，不必再建立同名 change。可直接執行：

```bash
openspec list --specs
openspec list
openspec status --change refactor-tb3-proposal --json
openspec show refactor-tb3-proposal
openspec validate --all --strict
python3 -m unittest discover -s tests -v
```

日後新增另一項功能時，才使用不同的 change 名稱，例如：

```bash
openspec new change integrate-chinese-intent-parser
openspec instructions proposal --change integrate-chinese-intent-parser --json
```

`status` 顯示 planning artifacts 完整，代表 proposal／specs／design／tasks 文件齊全；不代表 tasks 已全部實作。`validate` 檢查規格結構，不能代替整合測試。現有 Python 單元測試也不能證明語言準確率或實機導航成功率。

## 五、5／3／10 與需求的關係

| 類型 | 原內容 | 規格或驗收重點 |
|---|---|---|
| 核心 1 | 定位有不確定性 | TF／定位時效與終點驗證 |
| 核心 2 | 感測不到不等於沒有 | scan 時效、盲區與故障取消 |
| 核心 3 | 路徑需考慮車身 | 核對 footprint、地圖與路徑 |
| 核心 4 | 語意與控制分層 | 受限意圖與地點、工具白名單 |
| 核心 5 | 可靠性需重複評估 | mission-evaluation 全部需求 |
| 取捨 1 | 模組化／端對端 | 固定 Nav2，初版不訓練 RL |
| 取捨 2 | 地圖／無地圖 | 預建地圖、地點登錄與 map 一致性 |
| 取捨 3 | 保守距離／效率 | 固定參數，共同比較到達、碰撞與延遲 |
| 細節 Q1–Q2 | 打滑、定位與控制故障 | 交叉檢查 odometry／定位／TF |
| 細節 Q3–Q4 | 雷射盲區、窄門 | 感測範圍與 footprint 核對 |
| 細節 Q5–Q6 | 新障礙物、inflation | 即時底層處理與路徑檢查 |
| 細節 Q7–Q8 | 效率安全比較、sim-to-real | 固定條件、來源區分與不確定性 |
| 細節 Q9–Q10 | Agent 增益、歧義與取消 | B0/B1/B2、澄清與停止確認 |

## 六、交付與後續

本次可供檢查的內容是新版提案、OpenSpec 文件、README／DESIGN 導覽與驗證紀錄。原本期中 PDF／PPTX 留在原小組儲存庫，連結見 ORIGIN.md。

iLearning 作業頁標示個人作業，但題目沿用原分組專題。此個人儲存庫標明作者，透過 ORIGIN.md 揭露原團隊成果與個人整理範圍。繳交時以教師實際要求的網址或檔案格式為準；作業頁目前未明列必須重新產生 PDF／PPTX。

若需要畫面佐證，可在自己的終端機執行上列 version／status／validate 指令並截圖。這是方便檢查的建議，作業頁並未明訂必須附截圖。

## 七、來源

- [OpenSpec 官方專案](https://github.com/Fission-AI/OpenSpec)
- [OpenSpec CLI 文件](https://github.com/Fission-AI/OpenSpec/blob/main/docs/cli.md)
- [教師示範專案](https://github.com/huanchen1107/2026-11-11-DIC3-ProjectRefactor)
- [文獻與來源核對](REFERENCES.md)
