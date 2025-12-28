#!/usr/bin/env python3
# Dosyanın Python3 ile çalışacağını belirtir

import rclpy
# ROS2 Python kütüphanesi

from rclpy.node import Node
# ROS2 Node sınıfı

from turtlesim.msg import Pose
# turtlesim paketinden Pose mesaj tipi


class PoseSubscriber(Node):
    # Turtle'ın pozisyon bilgisini dinleyen node

    def __init__(self):
        # Node oluşturulduğunda çalışır
        super().__init__('pose_subscriber')

        # /turtle1/pose topic'ine subscriber oluşturulur
        # Mesaj tipi: Pose
        # Gelen mesajlar pose_callback fonksiyonuna gider
        self.subscription = self.create_subscription(
            Pose,
            "/turtle1/pose",
            self.pose_callback,
            10
        )

    def pose_callback(self, msg: Pose):
        # /turtle1/pose üzerinden yeni bir mesaj geldiğinde çalışır
        # Turtle'ın anlık pozisyon bilgisi ekrana yazdırılır
        self.get_logger().info(str(msg))


def main(args=None):
    # ROS2 sistemi başlatılır
    rclpy.init(args=args)

    # Subscriber node oluşturulur
    node = PoseSubscriber()

    # Node sürekli çalışır ve mesajları dinler
    rclpy.spin(node)

    # Node düzgün şekilde kapatılır
    node.destroy_node()
    rclpy.shutdown()


# Dosya direkt çalıştırılırsa main fonksiyonu çağrılır
if __name__ == '__main__':
    main()