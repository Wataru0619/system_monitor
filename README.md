# system_monitor

# 概要
このリポジトリは、ROS2用のパッケージです。  
システムのCPU使用率、メモリ使用率、送受信データ量の情報を取得し、指定したトピック(`/system_info`)にパブリッシュします。  

![test](https://github.com/Wataru0619/system_monitor/actions/workflows/test.yml/badge.svg)  
GithubActionsによるテスト結果バッジ

# 使用方法
1.以下のコマンドでシステム情報を出力します。　　
``` 
$ ros2 run system_monitor system_info_publisher  
``` 
2.受信側で以下のコマンドを入力し、システム情報を受信します。
```
$ ros2 topic echo /system_info
```
# 実行例
- 受信
```
data: 'CPU Usage: 0.0%

  Memory Usage: 0.45 GB / 15.49 GB (4.6% used)

  Network Traffic: Sent: 3.48 MB, Received: 26.26 MB

  '
---
data: 'CPU Usage: 0.0%

  Memory Usage: 0.45 GB / 15.49 GB (4.7% used)

  Network Traffic: Sent: 3.49 MB, Received: 26.26 MB

  '
```
# 動作環境
- OS: ubuntu-22.04  
- Python: 3.8  
- ROS2: Foxy Fitzroy  

# ライセンス
- このソフトウェアパッケージは、GPL3.0ライセンスの下、再頒布および使用が許可されます。
- このパッケージのテストには、以下のDockerイメージを使用しています。  
  [ryuichiueda/ubuntu22.04-ros2:latest](https://hub.docker.com/r/ryuichiueda/ubuntu22.04-ros2)
- © 2025 Wataru Suenagia

