#!/bin/bash
# SPDX-FileCopyrightText: 2025 Wataru Suenaga
# SPDX-License-Identifier: GPL-3.0-only

import rclpy
from rclpy.node import Node
import psutil
from std_msgs.msg import String

class SystemInfoPublisher(Node):
    def __init__(self):
        super().__init__('system_info_publisher')
        self.publisher_ = self.create_publisher(String, '/system_info', 10)
        # タイマーを設定して5秒ごとにpublish_system_infoを呼び出す
        self.timer = self.create_timer(5.0, self.publish_system_info)

    def publish_system_info(self):
        try:
            # CPU使用率を取得
            cpu_usage = psutil.cpu_percent(interval=1)  # 1秒間隔でCPU使用率を取得

            # メモリ使用量を取得
            memory_info = psutil.virtual_memory()
            memory_used = memory_info.used / (1024 ** 3)  # GB 単位に変換
            memory_total = memory_info.total / (1024 ** 3)  # GB 単位に変換
            memory_usage = memory_info.percent

            # ネットワーク使用量を取得
            net_info = psutil.net_io_counters()
            bytes_sent = net_info.bytes_sent / (1024 ** 2)  # MB単位に変換
            bytes_recv = net_info.bytes_recv / (1024 ** 2)  # MB単位に変換

            # メッセージを作成
            message = (f"CPU Usage: {cpu_usage}%\n"
                       f"Memory Usage: {memory_used:.2f} GB / {memory_total:.2f} GB ({memory_usage}% used)\n"
                       f"Network Traffic: Sent: {bytes_sent:.2f} MB, Received: {bytes_recv:.2f} MB\n")

        except Exception as e:
            message = f"Error retrieving system info: {str(e)}"

        # ROS2 メッセージとして送信
        msg = String()
        msg.data = message
        self.publisher_.publish(msg)
        self.get_logger().info('Success')

def main(args=None):
    rclpy.init(args=args)
    node = SystemInfoPublisher()
    try:
        rclpy.spin(node)  # ノードをスピンさせる
    except KeyboardInterrupt:
        pass  # 手動でCtrl+Cで終了した場合に備える
    finally:
        node.destroy_node()  # ノードを明示的に削除
        rclpy.shutdown()     # rclpyのシャットダウン

if __name__ == '__main__':
    main()

# This software package is licensed under the GPL-3.0 License, and redistribution and usage are permitted under its terms.
# © 2025:Wataru Suenaga
