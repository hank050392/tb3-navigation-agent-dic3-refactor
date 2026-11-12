# DIC3 驗證紀錄

日期：2026-11-12。以下輸出來自本次作業準備環境的實際執行。

## 一、環境與初始化

- Node.js：v24.22.1。
- npm：11.9.0。
- 已執行 npm 安裝 @fission-ai/openspec，實際解析版本為 2.0.0。
- 已執行 `openspec init --tools none` 及 `openspec new change refactor-tb3-proposal`，均成功建立文件結構。
- 為方便重現，使用說明固定安裝 2.0.0；這些動作未在使用者自己的電腦執行。

## 二、檢查結果

### openspec --version

Exit code: 0

```text
2.0.0
```

### openspec validate --all --strict

Exit code: 0

```text
✓ spec/offline-contract
✓ change/refactor-tb3-proposal
Totals: 2 passed, 0 failed (2 items)
```

### python3 -m unittest discover -s tests -v

Exit code: 0

```text
test_arbitrary_coordinate_is_rejected (test_agent_demo.ContractTests.test_arbitrary_coordinate_is_rejected) ... ok
test_bad_schema_types_are_rejected (test_agent_demo.ContractTests.test_bad_schema_types_are_rejected) ... ok
test_cancel_does_not_claim_real_stop (test_agent_demo.ContractTests.test_cancel_does_not_claim_real_stop) ... ok
test_clarify_does_not_dispatch (test_agent_demo.ContractTests.test_clarify_does_not_dispatch) ... ok
test_empty_question_is_rejected (test_agent_demo.ContractTests.test_empty_question_is_rejected) ... ok
test_failure_and_timeout_are_not_success (test_agent_demo.ContractTests.test_failure_and_timeout_are_not_success) ... ok
test_stale_or_blocked_does_not_dispatch (test_agent_demo.ContractTests.test_stale_or_blocked_does_not_dispatch) ... ok
test_unknown_landmark_never_dispatches (test_agent_demo.ContractTests.test_unknown_landmark_never_dispatches) ... ok
test_valid_goal_is_explicitly_mock (test_agent_demo.ContractTests.test_valid_goal_is_explicitly_mock) ... ok

----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

## 三、結果的適用範圍

OpenSpec 檢查通過的是一份既有離線規格及一個包含兩組新能力的 change。planning status 的 proposal／specs／design／tasks 皆為 done，僅表示文件齊全。tasks 中的 LLM、任務管理、Nav2 adapter 與實驗仍未完成，故沒有 archive。

原有 9 項測試全部通過，src 與 tests 未修改。未執行 Docker 建置、LLM 呼叫、ROS／Gazebo 或實機導航；因此本紀錄沒有導航成功率或語言準確率。
