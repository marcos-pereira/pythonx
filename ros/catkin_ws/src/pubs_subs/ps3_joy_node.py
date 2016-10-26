#!/usr/bin/env python

import rospy
import turtlesim.msg

from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

from sensor_msgs.msg import Joy

from std_msgs.msg import String

import hokuyo_node
import sensor_msgs.msg

# note on plain values:
# buttons are either 0 or 1
# button axes go from 0 to -1
# stick axes go from 0 to +/-1

#define PS3_BUTTON_SELECT            0
#define PS3_BUTTON_STICK_LEFT        1
#define PS3_BUTTON_STICK_RIGHT       2
#define PS3_BUTTON_START             3
#define PS3_BUTTON_CROSS_UP          4
#define PS3_BUTTON_CROSS_RIGHT       5
#define PS3_BUTTON_CROSS_DOWN        6
#define PS3_BUTTON_CROSS_LEFT        7
#define PS3_BUTTON_REAR_LEFT_2       8
#define PS3_BUTTON_REAR_RIGHT_2      9
#define PS3_BUTTON_REAR_LEFT_1       10
#define PS3_BUTTON_REAR_RIGHT_1      11
#define PS3_BUTTON_ACTION_TRIANGLE   12
#define PS3_BUTTON_ACTION_CIRCLE     13
#define PS3_BUTTON_ACTION_CROSS      14
#define PS3_BUTTON_ACTION_SQUARE     15
#define PS3_BUTTON_PAIRING           16

#define PS3_AXIS_STICK_LEFT_LEFTWARDS    0
#define PS3_AXIS_STICK_LEFT_UPWARDS      1
#define PS3_AXIS_STICK_RIGHT_LEFTWARDS   2
#define PS3_AXIS_STICK_RIGHT_UPWARDS     3
#define PS3_AXIS_BUTTON_CROSS_UP         4
#define PS3_AXIS_BUTTON_CROSS_RIGHT      5
#define PS3_AXIS_BUTTON_CROSS_DOWN       6
#define PS3_AXIS_BUTTON_CROSS_LEFT       7
#define PS3_AXIS_BUTTON_REAR_LEFT_2      8
#define PS3_AXIS_BUTTON_REAR_RIGHT_2     9
#define PS3_AXIS_BUTTON_REAR_LEFT_1      10
#define PS3_AXIS_BUTTON_REAR_RIGHT_1     11
#define PS3_AXIS_BUTTON_ACTION_TRIANGLE  12
#define PS3_AXIS_BUTTON_ACTION_CIRCLE    13
#define PS3_AXIS_BUTTON_ACTION_CROSS     14
#define PS3_AXIS_BUTTON_ACTION_SQUARE    15
#define PS3_AXIS_ACCELEROMETER_LEFT      16
#define PS3_AXIS_ACCELEROMETER_FORWARD   17
#define PS3_AXIS_ACCELEROMETER_UP        18
#define PS3_AXIS_GYRO_YAW                19

ps3_joystick_state = 0

class PS3Joy:
    acceleration_gain = 1
    ps3_joystick_state = Joy()

    # def __init__(self):      
        # init class parameters

    def callbackPS3Joy(self, data):        
        # print data
        PS3Joy.ps3_joystick_state = data

def hokuyoCb(self, data1):
    print data1    

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "\nI heard:\n")
    print data

def odometryCb(msg):
    print msg.pose.pose    

def readWritePS3JoyCmds(ps3_joystick_object, cmd_vel_to_turtle_pub):    

    # If you desire to get turtlesim pose uncomment this
    # rospy.Subscriber('/turtle1/pose',
    #              turtlesim.msg.Pose,                     
    #              callback)   

    # If you desire to get p3at odometry     
    # rospy.Subscriber('/odom',Odometry, odometryCb)

    # Try to get hokuyo laser scan data
    # rospy.Subscriber("/hokuyo_scan",sensor_msgs.msg.LaserScan,callback,10)

    # # # # # # # # # # #
    # PS3 joystick related
    ps3_joystick_sub = rospy.Subscriber('/joy', Joy, ps3_joystick_object.callbackPS3Joy, queue_size=3)
    # print ps3_joystick_state

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

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # Publish Twist message to turtlesim
    twist_msg_to_turtle = Twist()
    print ps3_joystick_object.ps3_joystick_state.buttons
    twist_msg_to_turtle.linear.x = 0        
    twist_msg_to_turtle.angular.z = 0
    # R2 - accelerate
    if ps3_joystick_object.ps3_joystick_state.buttons[9] == 1:                        
        ps3_joystick_object.acceleration_gain = ps3_joystick_object.acceleration_gain + 1                        
    # L2 - deaccelerate
    if ps3_joystick_object.ps3_joystick_state.buttons[8] == 1:                
        if ps3_joystick_object.acceleration_gain > 0:                   
            ps3_joystick_object.acceleration_gain = ps3_joystick_object.acceleration_gain - 1        
    # CROSS UP    
    if ps3_joystick_object.ps3_joystick_state.buttons[4] == 1:        
        twist_msg_to_turtle.linear.x = 1*ps3_joystick_object.acceleration_gain                       
    # CROSS DOWN
    if ps3_joystick_object.ps3_joystick_state.buttons[6] == 1:
        twist_msg_to_turtle.linear.x = -1*ps3_joystick_object.acceleration_gain                   
    # CROSS RIGHT        
    if ps3_joystick_object.ps3_joystick_state.buttons[5] == 1:
        twist_msg_to_turtle.angular.z = -1*ps3_joystick_object.acceleration_gain 
    # CROSS LEFT
    if ps3_joystick_object.ps3_joystick_state.buttons[7] == 1:
        twist_msg_to_turtle.angular.z = 1*ps3_joystick_object.acceleration_gain                  

    # twist_msg_to_turtle.linear.x = 1
    # twist_msg_to_turtle.linear.y = 0
    twist_msg_to_turtle.linear.z = 0
    twist_msg_to_turtle.angular.x = 0
    twist_msg_to_turtle.angular.y = 0
    # twist_msg_to_turtle.angular.z = 0
    cmd_vel_to_turtle_pub.publish(twist_msg_to_turtle)

    # Publish Twist message to pioneer
    twist_msg_to_p3at = Twist()
    twist_msg_to_p3at.linear.x = -1
    twist_msg_to_p3at.linear.y = 0
    twist_msg_to_p3at.linear.z = 0
    twist_msg_to_p3at.angular.x = 0
    twist_msg_to_p3at.angular.y = 0
    twist_msg_to_p3at.angular.z = 1
    # cmd_vel_to_p3at_pub.publish(twist_msg_to_p3at)

    # Hello world message test
    # hello_str = "hello world %s" % rospy.get_time()
    # rospy.loginfo(hello_str)
    # Reference of original code: http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29        
    # pub.publish(hello_str)

def mainFunction():    
    pub = rospy.Publisher('chatter', String, queue_size=10)

    # # # # # # # # # # #
    # PS3 joystick related
    ps3_joystick_sub = rospy.Subscriber('/joy', Joy, queue_size=1)
    ps3_object = PS3Joy()

    # # # # # # # # # # #
    # Gazebo p3at sim related

    # pose_to_turtle_pub = rospy.Publisher(turtlename, turtlesim.msg.Pose, queue_size=10)
    cmd_vel_to_p3at_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)


    # # # # # # # # # # #
    # Turtlesim sim related

    # Get turtlesim pose
    turtlename = 'myturtle'
    sub2 = rospy.Subscriber(turtlename, turtlesim.msg.Pose, queue_size=1)
    cmd_vel_to_turtle_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
    
    # # # # # # # # # # # #
    # Hello world related
    rospy.init_node('talker', anonymous=True)

    # Rate for publish/subscribe
    rate = rospy.Rate(10) # 10hz

    ps3_setup_time = 20
    time_counter = 0    
    while not rospy.is_shutdown():
        ps3_joystick_sub = rospy.Subscriber('/joy', Joy, ps3_object.callbackPS3Joy, queue_size=3)
        if time_counter < ps3_setup_time:
            time_counter = time_counter + 1
        else:
            readWritePS3JoyCmds(ps3_object, cmd_vel_to_turtle_pub)   

        rate.sleep()

if __name__ == '__main__':
    try:
        mainFunction()
    except rospy.ROSInterruptException:
        pass