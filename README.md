# DIC3：TB3 專題提案 OpenSpec 個人改版

**蕭丞皓｜7115064186｜2026-11-12**

本作業以先前第 7 組「TurtleBot3 Burger 室內導航與任務決策 AI Agent」為基礎，個人完成提案重整與 OpenSpec 規格化。原小組成果及本次改版範圍見 [來源與貢獻說明](docs/ORIGIN.md)。

## 作業入口

| 文件 | 內容 |
|---|---|
| [新版提案](PROPOSAL.md) | A–F、中英文摘要、Introduction、Related Work、5 核心／3 爭論／10 問題 |
| [作業對照與操作](docs/DIC3_OPENSPEC.md) | 教師要求、檔案對照、安裝與重現指令 |
| [系統設計](DESIGN.md) | 架構、流程與 OpenSpec 對照 |
| [OpenSpec 變更提案](openspec/changes/refactor-tb3-proposal/proposal.md) | 動機與能力範圍 |
| [OpenSpec 技術設計](openspec/changes/refactor-tb3-proposal/design.md) | 決策、工作流程、驗收與限制 |
| [任務清單](openspec/changes/refactor-tb3-proposal/tasks.md) | 已完成的文件工作與待實作的整合 |
| [驗證紀錄](docs/DIC3_VALIDATION.md) | CLI 驗證與原有離線測試 |

## 狀態與重現

本次完成文件與規格改版。繼承的 Python 範例只做 JSON 驗證與 mock 回報，尚未整合 LLM、ROS 2 或實體導航。現有離線契約在 `openspec/specs/`，待整合能力在 `openspec/changes/`；規格存在不代表功能已完成。

需 Python 3.10 以上；OpenSpec 的 npm 安裝需 Node.js 22.12.0 以上。

```bash
npm install -g @fission-ai/openspec@2.0.0
openspec validate --all --strict
python3 -m unittest discover -s tests -v
python3 src/agent_demo.py --request examples/navigate.json --scenario ready
```

指令從儲存庫根目錄執行。mock ARRIVED 不代表實機成功；測試結果不能當成語言準確率或導航成功率。完整研究引用見 [REFERENCES.md](docs/REFERENCES.md)。
