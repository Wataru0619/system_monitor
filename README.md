# system_monitor

# 概要
このリポジトリは、ROS2用のパッケージです。  
システムのCPU使用率　メモリ使用率　送受信データ量の情報を取得し、指定したトピック(`/system_info`)にパブリッシュします。

# 内容
- .github/workflows  
GithubActions用プログラム
- resource  
リソースファイル（今回は使用しない））
- system_monitor
システムのCPU使用率　メモリ使用率　送受信データ量の情報を取得し、指定したト>
ピック(`/system_info`)にパブリッシュするプログラム。
- test  
テスト用プログラム
- COPYING  
ライセンスに関する文章
- README.md  
この説明書
- package.xml  
ROS2パッケージ設定ファイル
- setup.cfg  
Pythonパッケージ設定ファイル
- setup.py  
Pythonパッケージインストールスクリプト  

![test](https://github.com/Wataru0619/system_monitor/actions/workflows/test.yml/badge.svg)  
GithubActionsによるテスト結果バッジ
# 使用方法
1.ROS2のワークスペースにこのパッケージを追加します。  
2.以下のコマンドでシステム情報を出力します。　　
``` 
$ ros2 run system_monitor system_info_publisher  
``` 
3.受信側で以下のコマンドを入力し、システム情報を受信する。
```
$ ros2 topic echo /system_info
```
# 実行例
- 送信  
```
[INFO] [1736085754.506566148] [system_info_publisher]: Success
[INFO] [1736085759.491369972] [system_info_publisher]: Success

```
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
- OS: Linux  
- Python: テスト済みバージョン　3.7~3.13  

# テスト環境
- ubuntu-22.04  

# ライセンス
- このソフトウェアパッケージは，GPL3.0ライセンスの下，再頒布および使用が許可されます．
- © 2025 Wataru Suenagia
