#!/usr/bin/env python
#-*- coding:utf-8 -*-

import rospy
import cv2
import numpy as np
import os, rospkg
import json
import math
import random
import tf

from cv_bridge import CvBridgeError
from sklearn import linear_model

from nav_msgs.msg import Odometry,Path
from sensor_msgs.msg import CompressedImage
from geometry_msgs.msg import PoseStamped,Point
from morai_msgs.msg import CtrlCmd, EgoVehicleStatus

class IMGParser:
    def __init__(self, pkg_name = 'final'):
        self.image_sub = rospy.Subscriber("/image_jpeg/compressed", CompressedImage, self.callback)
        rospy.Subscriber("odom", Odometry, self.odom_callback)
        self.path_pub = rospy.Publisher('/lane_path', Path, queue_size=30)

        self.img_bgr = None
        self.img_lane = None
        self.edges = None 
        self.is_status = False

        self.lower_wlane = np.array([0,0,205])
        self.upper_wlane = np.array([30,60,255])

        self.lower_ylane = np.array([0,70,120])# ([0,60,100])
        self.upper_ylane = np.array([40,195,230])# ([40,175,255])

        self.crop_pts = np.array([[[0,480],[0,350],[280,200],[360,200],[640,350],[640,480]]])

    def callback(self, msg):
        try:
            np_arr = np.fromstring(msg.data, np.uint8)
            self.img_bgr = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        except CvBridgeError as e:
            print(e)