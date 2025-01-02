import rclpy
from rclpy.node import Node
import subprocess
import psutil
from std_msgs.msg import String

class SystemInfoPublisher(Node):
    def __init__(self):
        super().__init__('system_info_publisher')
        self.publisher_ = self.create_publisher(String, '/system_info', 10)
        self.publish_system_info()

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

            # システムの稼働時間を取得
            uptime = subprocess.check_output("uptime -p", shell=True).decode().strip()

            # メッセージを作成
            message = (f"CPU Frequency: {cpu_freq} MHz\n"
                       f"CPU Cores: {cpu_cores}\n"
                       f"Memory Usage: {memory_used:.2f} GB / {memory_total:.2f} GB ({memory_usage}% used)\n"
                       f"Uptime: {uptime}")

        except Exception as e:
            message = "Error retrieving system info."

        # ROS2 メッセージとして送信
        msg = String()
        msg.data = message
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published system info: {message}')

def main(args=None):
    rclpy.init(args=args)
    node = SystemInfoPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


