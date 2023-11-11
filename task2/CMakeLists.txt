cmake_minimum_required(VERSION 2.8.3)
project(my_turtle_controller)

find_package(catkin REQUIRED COMPONENTS
  rospy
  geometry_msgs
  turtlesim
)

catkin_package()

install(PROGRAMS
  src/draw_circle_node.py
  src/subscribe_cmd_vel_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
