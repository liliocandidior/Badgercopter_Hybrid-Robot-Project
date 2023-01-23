#! /usr/bin/env python3

"""
 * File: offb_node.py
 * Stack and tested in Gazebo 9 SITL
"""

import rospy
from geometry_msgs.msg import PoseStamped
from mavros_msgs.msg import State
from mavros_msgs.srv import CommandBool, CommandBoolRequest, SetMode, SetModeRequest

aerial_state = PoseStamped()
ground_state = PoseStamped()
current_state = State()

def state_cb(msg):
    global current_state
    current_state = msg

def mo_aerial_cb(msg):
    global aerial_state
    aerial_state = msg
    
def mo_ground_cb(msg):
    global ground_state
    ground_state = msg

if __name__ == "__main__":
    rospy.init_node("offb_node_py")
    
    state_sub = rospy.Subscriber("mavros/state", State, callback = state_cb)
    mo_aerial_sub = rospy.Subscriber("mocap_node/aerial/pose", PoseStamped, callback = mo_aerial_cb)
    mo_ground_sub = rospy.Subscriber("mocap_node/ground/pose", PoseStamped, callback = mo_ground_cb)

    setpoint_pub = rospy.Publisher("mavros/setpoint_position/local", PoseStamped, queue_size=10)
    mo_aerial_pub = rospy.Publisher("mavros/mocap/pose", PoseStamped, queue_size=10)
    rospy.loginfo("sub and pub setup complete")
    
    rospy.wait_for_service("/mavros/cmd/arming")
    arming_client = rospy.ServiceProxy("mavros/cmd/arming", CommandBool)    

    rospy.wait_for_service("/mavros/set_mode")
    set_mode_client = rospy.ServiceProxy("mavros/set_mode", SetMode)
    rospy.loginfo("arm and mode setup complete")
    

    # Setpoint publishing MUST be faster than 2Hz
    rate = rospy.Rate(20)

    # Wait for Flight Controller connection
    while(not rospy.is_shutdown() and not current_state.connected):
        rate.sleep()
    rospy.loginfo("Flag A")

    setpoint = PoseStamped()
    rospy.loginfo("Flag B")

    rospy.loginfo("pre-loop complete")

    # Send a few setpoints before starting
    for i in range(100):   
        if(rospy.is_shutdown()):
            break
        mo_aerial_pub.publish(aerial_state)
        setpoint_pub.publish(setpoint)
        rate.sleep()

    offb_set_mode = SetModeRequest()
    offb_set_mode.custom_mode = 'OFFBOARD'

    arm_cmd = CommandBoolRequest()
    arm_cmd.value = True

    last_req = rospy.Time.now()
    rospy.loginfo("pre-start complete")

    while(not rospy.is_shutdown()):
        if(current_state.mode != "OFFBOARD" and (rospy.Time.now() - last_req) > rospy.Duration(5.0)):
            if(set_mode_client.call(offb_set_mode).mode_sent == True):
                rospy.loginfo("OFFBOARD enabled")
            
            last_req = rospy.Time.now()
        else:
            if(not current_state.armed and (rospy.Time.now() - last_req) > rospy.Duration(5.0)):
                if(arming_client.call(arm_cmd).success == True):
                    rospy.loginfo("Vehicle armed")
            
                last_req = rospy.Time.now()
	
        setpoint.pose.position.x = ground_state.pose.position.x
        setpoint.pose.position.y = ground_state.pose.position.y
        setpoint.pose.position.z = ground_state.pose.position.z+0.5
        #mo_aerial_pub.publish(aerial_state)
        setpoint_pub.publish(setpoint)
	
        rate.sleep()

