#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import math

def draw_circle():
    rospy.init_node('draw_circle_node', anonymous=True)
    rate = rospy.Rate(1)  

    cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    while not rospy.is_shutdown():
        twist_cmd = Twist()
        twist_cmd.linear.x = 1.0 
        twist_cmd.angular.z = 1.0  
        cmd_vel_pub.publish(twist_cmd)

        rate.sleep()

if __name__ == '__main__':
    try:
        draw_circle()
    except rospy.ROSInterruptException:
        pass
