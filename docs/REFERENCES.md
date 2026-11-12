# 參考資料

[1] Yao, S., et al. (2023). ReAct: Synergizing Reasoning and Acting in Language Models. ICLR 2023; arXiv:2210.03629.
https://arxiv.org/abs/2210.03629

[2] Ahn, M., et al. (2022). Do As I Can, Not As I Say: Grounding Language in Robotic Affordances. CoRL 2022; arXiv:2204.01691.
https://arxiv.org/abs/2204.01691

[3] Pollini, D., Guterres, B. V., Guerra, R. S., & Grando, R. B. (2025). Reducing Latency in LLM-Based Natural Language Commands Processing for Robot Navigation. arXiv:2506.00075; accepted to INDIN 2025.
https://arxiv.org/abs/2506.00075

[4] Macenski, S., Martín, F., White, R., & Clavero, J. G. (2020). The Marathon 2: A Navigation System. IROS 2020; arXiv:2003.00368.
https://arxiv.org/abs/2003.00368

[5] Macenski, S., & Jambrecic, I. (2021). SLAM Toolbox: SLAM for the dynamic world. Journal of Open Source Software, 6(61), 2783; doi:10.21105/joss.02783.
https://joss.theoj.org/papers/10.21105/joss.02783

[6] Xiao, X., et al. (2022). Autonomous Ground Navigation in Highly Constrained Spaces: Lessons Learned from the BARN Challenge at ICRA 2022. IEEE Robotics & Automation Magazine; arXiv:2208.10473.
https://arxiv.org/abs/2208.10473

[7] El-Hariry, M., et al. (2025). RoboRAN: A Unified Robotics Framework for Reinforcement Learning-Based Autonomous Navigation. arXiv:2505.14526v2; accepted at TMLR.
https://arxiv.org/abs/2505.14526

[8] ROBOTIS (官方文件). TurtleBot3 Features and Navigation. 硬體規格與導航流程；實際 LDS 型號依實機確認.
https://emanual.robotis.com/docs/en/platform/turtlebot3/features/

[9] ROS Navigation maintainers (官方文件). Nav2 Tuning Guide. 車身 footprint、代價地圖與障礙物膨脹.
https://docs.nav2.org/jazzy/configuration_and_development/tuning_guide/

[10] ROS Navigation maintainers (官方文件). Nav2 Simple Commander API. 任務呼叫與回饋；使用前須核對已安裝 ROS 發行版.
https://docs.nav2.org/jazzy/configuration_and_development/simple_commander_api/simple_commander_api/

[11] ROS Navigation maintainers (官方程式庫). Nav2 Collision Monitor. 感測資料監測與減速／停止；不是安全認證保證.
https://github.com/ros-navigation/navigation2/blob/main/nav2_collision_monitor/README.md

[12] Xiao, X., and BARN organizers (2026). The BARN Challenge 2026. 標準化導航測試、傳統與學習方法基準.
https://people.cs.gmu.edu/~xiao/Research/BARN_Challenge/BARN_Challenge26.html

查閱：2026-10-30。

## DIC3 核對與工具來源（2026-11-12）

- [1]–[7]：核對 arXiv／JOSS 原始來源的標題、方法摘要與平台範圍；[7] 依 v2 改為 RoboRAN。未將文獻成效當成本組結果。
- [8]、[12]：核對 ROBOTIS 平台文件及 BARN 2026 官方頁面。
- [9]–[11]：原提案保留的 API／調校參考；須依實際 ROS 發行版再核對，尚未作為本組已整合證據。
- OpenSpec 官方專案：https://github.com/Fission-AI/OpenSpec
- OpenSpec CLI 參考：https://github.com/Fission-AI/OpenSpec/blob/main/docs/cli.md
- 教師示範：https://github.com/huanchen1107/2026-11-11-DIC3-ProjectRefactor

本次使用 OpenSpec 2.0.0。舊教材可能使用不同 slash command；本專案說明採實際 CLI 的 new／status／validate／instructions 指令。
