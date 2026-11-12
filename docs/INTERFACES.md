# 工具介面與整合契約

以下是預計介面，尚未連接 ROS 2。

| 工具 | 輸入 | 必要輸出 |
|---|---|---|
| list_landmarks | map_id | ID、別名、registry_version |
| get_robot_status | 無 | scan_age、pose_age、tf_ok、nav_active、task_active、timestamp |
| get_path | landmark_id | valid、map_id、path_id、error、timestamp |
| navigate_to_landmark | landmark_id、mission_id | accepted、goal_id、error |
| cancel_navigation | mission_id | request_accepted、terminal_result、stop_observed |
| read_mission_result | mission_id | action_state、final_pose、timestamp、evidence_id |

地點 ID 在 gateway 轉為 PoseStamped，frame_id 使用地點表指定的 map。
正式 adapter 可參考 Nav2 Simple Commander 的 goToPose、getFeedback、isTaskComplete、getResult、cancelTask，
但應核對實際版本，檢查例外與 None。任務完成後仍需讀結果。

## 時間與故障

資料時效依 ROS 時間計算，控制流程 deadline 用可單調前進的計時器。
模擬 use_sim_time 與實機設定分開。不能把模擬暫停誤認成新鮮實機資料。
timeout、斷線、拒收與定位異常均有不同 error code；不得自動改為成功。
取消必須觀察 action 結果與停止；若無法確認，回報 FAULT 並通知操作員。

## Schema

navigate：僅 intent 與 landmark_id 兩欄；ID 必須存在。
cancel：僅 intent 一欄。clarify：intent 與非空 question。
reject：intent 與非空 reason。未定義 intent 或額外欄位拒絕。
正式 LLM adapter 必須設定輸出長度、呼叫 timeout、固定版本與 prompt。
