#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Point


class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.subscription = self.create_subscription(
            Point,
            '/point',
            self.listener_callback,
            10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.linear_x = 0.0
        self.angular_z = 0.0

    def listener_callback(self, msg):
        if msg.z == 0.0:
            self.linear_x = 0.0
            self.get_logger().info("Postój")
        elif msg.y < 240.0:
            self.linear_x = 0.5
            self.get_logger().info("Jazda do przodu")
        else:
            self.linear_x = -0.5
            self.get_logger().info("Jazda do tylu")

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = self.linear_x
        msg.angular.z = self.angular_z
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = TurtleController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()