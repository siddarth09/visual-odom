#!/usr/bin/python3
import cv_bridge
import rospy

from sensor_msgs.msg import Image
from cv_bridge import CvBridge,CvBridgeError
import cv2

bridge = CvBridge()
def callback(msg):

    frame = bridge.imgmsg_to_cv2(msg, "bgr8")
    if frame is None:
        rospy.loginfo("NO IMAGE RETURNED FROM ORB")

    cv2.imshow('Video Feed', frame)
    cv2.waitKey(1)
    rospy.loginfo('Image feed received!')

    image=bridge.cv2_to_imgmsg(frame,encoding="passthrough")

    image_pub=rospy.Publisher('/camera/image_raw',Image,queue_size=10)

    image_pub.publish(image)
    




def orbSlam():
    rospy.init_node('video_of_orb')
    #first parameter is the topic you want to subcribe sensor_msgs/Image from
    rospy.Subscriber('/orb_slam2_mono/debug_image', Image, callback)
    rospy.spin()
if __name__ == '__main__':
    orbSlam()
