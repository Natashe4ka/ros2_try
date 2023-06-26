import rclpy
from rclpy.node import Node
import time
from std_msgs.msg import String

rclpy.init()
nd = Node('minimal_publisher')
pub = nd.create_publisher(String, 'welcome_topic', 10)

msg = String()
msg.data = "hello world"

while True:
    time.sleep(1)
    pub.publish(msg)