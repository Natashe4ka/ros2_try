import rclpy
from rclpy.node import Node
#import time
from std_msgs.msg import String

rclpy.init()

def callback(msg):
    print ('I heard: "%s"' % msg.data)

nd = Node('minimal_subscriber')
sub = nd.create_subscription(String, '/welcome_topic', callback, 10)

msg = String()
rclpy.spin(nd)
