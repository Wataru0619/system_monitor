import rclpy
from rclpy.node import Node
from rclpy.timer import Timer
import subprocess
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
            # `lscpu` コマンドを使用して CPU の周波数とコア数を取得
            result = subprocess.run(['lscpu'], stdout=subprocess.PIPE)
            output = result.stdout.decode('utf-8')

            cpu_freq = None
            cpu_cores = None

            # "CPU MHz" と "CPU(s)" 行を抽出
            for line in output.splitlines():
                if "CPU MHz" in line:
                    cpu_freq = line.split(":")[1].strip()
                if "CPU(s)" in line:
                    cpu_cores = line.split(":")[1].strip()

            if cpu_freq is None:
                cpu_freq = "Unknown"
            if cpu_cores is None:
                cpu_cores = "Unknown"

            # メモリ使用量を取得
            memory_info = psutil.virtual_memory()
            memory_used = memory_info.used / (1024 ** 3)  # GB 単位に変換
            memory_total = memory_info.total / (1024 ** 3)  # GB 単位に変換
            memory_usage = memory_info.percent

            # メッセージを作成
            message = (f"CPU Frequency: {cpu_freq} MHz\n"
                       f"CPU Cores: {cpu_cores}\n"
                       f"Memory Usage: {memory_used:.2f} GB / {memory_total:.2f} GB ({memory_usage}% used)\n")

        except Exception as e:
            message = f"Error retrieving system info: {str(e)}"

        # ROS2 メッセージとして送信
        msg = String()
        msg.data = message
        self.publisher_.publish(msg)
        self.get_logger().info('success published')

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



