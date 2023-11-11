#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def cmd_vel_callback(msg):
    rospy.loginfo("Linear Velocity (x): %f", msg.linear.x)
    rospy.loginfo("Angular Velocity (z): %f", msg.angular.z)

def subscribe_cmd_vel():
    rospy.init_node('subscribe_cmd_vel_node', anonymous=True)
    
    rospy.Subscriber('/cmd_vel', Twist, cmd_vel_callback)

    rospy.spin()

if __name__ == '__main__':
    try:
        subscribe_cmd_vel()
    except rospy.ROSInterruptException:
        pass
