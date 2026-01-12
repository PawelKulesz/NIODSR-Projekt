#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Point
import cv2
import numpy as np
from cv_bridge import CvBridge


class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('camera_node')

        self.declare_parameter('square_size', 200)

        self.window_name = "camera"
        self.bridge = CvBridge()

        self.publisher_ = self.create_publisher(Point, '/point', 10)

        self.subscription = self.create_subscription(
            Image,
            'image_raw',
            self.listener_callback,
            10)
        self.subscription

        self.point = None

        self.timer = self.create_timer(0.05, self.timer_callback)

    def listener_callback(self, image_data):
        pass


    def timer_callback(self):
        cv_image = np.zeros((512, 700, 3), np.uint8)

        size = self.get_parameter('square_size').value

        if self.point is not None:
            cv2.rectangle(cv_image, self.point,
                          (self.point[0] + size, self.point[1] + size),
                          (0, 255, 0), 3)

        cv2.imshow(self.window_name, cv_image)
        cv2.waitKey(1)
        cv2.setMouseCallback(self.window_name, self.draw_rectangle)

    def draw_rectangle(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.point = (x, y)

            msg = Point()
            msg.x = float(x)
            msg.y = float(y)
            self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()