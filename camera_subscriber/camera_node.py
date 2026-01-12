#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Point
import cv2
import numpy as np
from cv_bridge import CvBridge


class CameraArucoNode(Node):
    def __init__(self):
        super().__init__('camera_node')
        self.publisher_ = self.create_publisher(Point, '/point', 10)
        self.timer = self.create_timer(0.05, self.timer_callback)

        # Inicjalizacja kamery
        self.cap = cv2.VideoCapture(0)
        self.bridge = CvBridge()

        # POPRAWKA DLA STARSZYCH WERSJI OPENCV (ROS 2 Humble standard)
        # Zamiast getPredefinedDictionary -> Dictionary_get
        self.aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
        # Zamiast DetectorParameters -> DetectorParameters_create
        self.aruco_params = cv2.aruco.DetectorParameters_create()

        self.get_logger().info("Kamera wystartowała (Legacy API). Pokaż znacznik ArUco!")

    def timer_callback(self):
        ret, frame = self.cap.read()
        if not ret:
            return

        frame = cv2.resize(frame, (640, 480))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #wykrywanie aruco
        corners, ids, rejected = cv2.aruco.detectMarkers(
            gray, self.aruco_dict, parameters=self.aruco_params)

        marker_visible = 0.0
        target_y = 240.0

        if ids is not None:
            marker_visible = 1.0
            #srodek markera
            c = corners[0][0]
            center_x = int((c[0][0] + c[1][0] + c[2][0] + c[3][0]) / 4)
            center_y = int((c[0][1] + c[1][1] + c[2][1] + c[3][1]) / 4)

            target_y = float(center_y)

            cv2.aruco.drawDetectedMarkers(frame, corners, ids)
            cv2.circle(frame, (center_x, center_y), 5, (0, 255, 0), -1)

            cv2.line(frame, (0, 240), (640, 240), (0, 0, 255), 2)

        msg = Point()
        msg.x = 0.0
        msg.y = target_y
        msg.z = marker_visible
        self.publisher_.publish(msg)

        cv2.imshow('ArUco Control', frame)
        cv2.waitKey(1)

    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()


def main(args=None):
    rclpy.init(args=args)
    node = CameraArucoNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()