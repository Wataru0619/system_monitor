import unittest
from rclpy.node import Node
from rclpy import init, shutdown
from rclpy.executors import SingleThreadedExecutor
from std_msgs.msg import String
from system_monitor.system_info_publisher import SystemInfoPublisher

class TestSystemInfoPublisher(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        init()
        cls.executor = SingleThreadedExecutor()

    @classmethod
    def tearDownClass(cls):
        shutdown()

    def setUp(self):
        self.node = SystemInfoPublisher()
        self.executor.add_node(self.node)

    def tearDown(self):
        self.executor.remove_node(self.node)
        self.node.destroy_node()

    def test_publisher_initialization(self):
        publishers = self.node.get_topic_names_and_types()
        topic_found = any('/system_info' in topic for topic, types in publishers)
        self.assertTrue(topic_found, "The '/system_info' topic was not initialized properly.")

    def test_message_publishing(self):
        messages = []

        class TestSubscriber(Node):
            def __init__(self):
                super().__init__('test_subscriber')
                self.subscription = self.create_subscription(
                    String,
                    '/system_info',
                    self.callback,
                    10
                )
                self.messages = []

            def callback(self, msg):
                self.messages.append(msg.data)

        test_subscriber = TestSubscriber()
        self.executor.add_node(test_subscriber)

        try:
            for _ in range(5):
                self.executor.spin_once(timeout_sec=0.1)
                messages = test_subscriber.messages
                if messages:
                    break
        finally:
            self.executor.remove_node(test_subscriber)
            test_subscriber.destroy_node()

        self.assertTrue(messages, "No messages were received on '/system_info'.")
        self.assertIn("CPU Frequency", messages[0], "Published message does not contain expected system information.")

