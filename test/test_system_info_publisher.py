import rclpy
from rclpy.node import Node
import pytest
from unittest.mock import patch, MagicMock
from std_msgs.msg import String
from system_monitor.system_info_publisher import SystemInfoPublisher

# モック用のfixture
@pytest.fixture
def mock_subprocess_run():
    with patch("subprocess.run") as mock_run:
        yield mock_run

@pytest.fixture
def mock_psutil_virtual_memory():
    with patch("psutil.virtual_memory") as mock_memory:
        yield mock_memory

@pytest.fixture
def system_info_publisher_node():
    rclpy.init()
    node = SystemInfoPublisher()
    yield node
    node.destroy_node()
    rclpy.shutdown()

# SystemInfoPublisherのテスト
def test_system_info_publisher(mock_subprocess_run, mock_psutil_virtual_memory, system_info_publisher_node):
    # モックを設定
    mock_subprocess_run.return_value = MagicMock(stdout=b"CPU MHz: 2400\nCPU(s): 4")
    mock_psutil_virtual_memory.return_value = MagicMock(used=4 * 1024**3, total=8 * 1024**3, percent=50)
    
    # メッセージを受け取るためのコールバック
    msg = None
    def listener_callback(msg_in):
        nonlocal msg
        msg = msg_in
    
    # サブスクライバーを作成
    system_info_publisher_node.create_subscription(String, '/system_info', listener_callback, 10)
    
    # テスト対象メソッドを呼び出し
    system_info_publisher_node.publish_system_info()

    # メッセージが送信されたことを確認
    assert msg is not None
    assert "CPU Frequency" in msg.data
    assert "CPU Cores" in msg.data
    assert "Memory Usage" in msg.data
    assert "Uptime" in msg.data
    
    # subprocess.runが適切に呼び出されたか確認
    mock_subprocess_run.assert_called_with(['lscpu'], stdout=subprocess.PIPE)
    
    # psutil.virtual_memoryが呼び出されたか確認
    mock_psutil_virtual_memory.assert_called_once()

