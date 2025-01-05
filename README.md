# system_monitor

# 概要
このリポジトリは、ROS2用のパッケージです。  
システムのCPU周波数、コア数、メモリ使用量などの情報を取得し、指定したトピック(`/system_info`)にパブリッシュします。

# 内容
- .github/workflows  
GithubActions用プログラム
- resource  
- system_monitor  
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

```
- 受信
```
  
```
# 動作環境
- OS: Linux  
- Python: テスト済みバージョン　3.7~3.13  

# テスト環境
- ubuntu-22.04  

# ライセンス
- このソフトウェアパッケージは，GPL3.0ライセンスの下，再頒布および使用が許可されます．
- © 2025 Wataru Suenagia
