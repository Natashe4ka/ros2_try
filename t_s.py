import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time


def turtle_curcle (radius):
    rclpy.init()
    nd = Node('turtl_node')
    pub = nd.create_publisher(Twist, '/turtle1/cmd_vel', 10)
    #rate = nd.create_rate(0.5)
    vel = Twist()
    while rclpy.ok():
        vel.linear.x = radius
        vel.angular.z = 1.0
        pub.publish (vel)
        time.sleep(0.5)

turtle_curcle(1.0)  