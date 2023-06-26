import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

import time

l = 0

first_time = True

rclpy.init()
nd = Node('turtle_node')
pub = nd.create_publisher(Twist, '/turtle1/cmd_vel', 10)

def callback(msg):
    global l
    l = msg.x
    if first_time:
        l_init = msg.x
        first_time = False
    print(l)


nd.create_subscription(Pose, '/turtle1/pose', callback, 10)

#rate = nd.create_rate(0.5)
def mover(vel):
    pub_vel=Twist()
    pub_vel.linear.x = vel
    pub.publish(pub_vel)

def reg():
    if l < 6.5:
        mover(0.1)
    else:
        mover(0.0)

while rclpy.ok():
    reg()
    rclpy.spin_once(nd)
    time.sleep(0.5)