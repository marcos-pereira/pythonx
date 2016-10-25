#!/usr/bin/env python

import rospy
import turtlesim.msg

from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

from std_msgs.msg import String

import hokuyo_node
import sensor_msgs.msg

def hokuyoCb(self, data1):
    print data1    

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "\nI heard:\n")
    print data

def odometryCb(msg):
    print msg.pose.pose    

def talker():    
    pub = rospy.Publisher('chatter', String, queue_size=10)

    # # # # # # # # # # #
    # Gazebo p3at sim related

    turtlename = 'myturtle'
    # pose_to_turtle_pub = rospy.Publisher(turtlename, turtlesim.msg.Pose, queue_size=10)
    cmd_vel_to_p3at = rospy.Publisher('/cmd_vel', Twist, queue_size=1)


    # Get turtlesim pose
    sub2 = rospy.Subscriber(turtlename, turtlesim.msg.Pose, queue_size=1)

    
    # # # # # # # # # # # #
    # Hello world related
    rospy.init_node('talker', anonymous=True)

    # Rate for publish/subscribe
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        # If you desire to get turtlesim pose uncomment this
        # rospy.Subscriber('/turtle1/pose',
        #              turtlesim.msg.Pose,                     
        #              callback)   

        # If you desire to get p3at odometry     
        # rospy.Subscriber('/odom',Odometry, odometryCb)

        rospy.Subscriber("/hokuyo_scan",sensor_msgs.msg.LaserScan,callback,10)

        # Try to publish pose to turtlesim 
        # but does not make sense since turtlesim subscribe only /turtle1/cmd_vel
        # x = 1;
        # y = 0;
        # theta = 0;
        # linear_velocity = 1;
        # angular_velocity = 0;
        # cmd_vel_msg = ['1','0','0','1','0'];        
        # cmd_vel_msg = [str(x), str(y), str(theta), str(linear_velocity), str(angular_velocity)];        
        # cmd = turtlesim.msg.Pose
        # cmd.x = x
        # cmd.y = y
        # cmd.theta = theta
        # cmd.linear_velocity = linear_velocity
        # cmd.angular_velocity = angular_velocity

        # Publish Twist message to turtlesim
        twist_msg_to_p3at = Twist()
        twist_msg_to_p3at.linear.x = -1
        twist_msg_to_p3at.linear.y = 0
        twist_msg_to_p3at.linear.z = 0
        twist_msg_to_p3at.angular.x = 0
        twist_msg_to_p3at.angular.y = 0
        twist_msg_to_p3at.angular.z = 1
        cmd_vel_to_p3at.publish(twist_msg_to_p3at)

        # Hello world message test
        # hello_str = "hello world %s" % rospy.get_time()
        # rospy.loginfo(hello_str)
        # Reference of original code: http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29        
        # pub.publish(hello_str)

        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass