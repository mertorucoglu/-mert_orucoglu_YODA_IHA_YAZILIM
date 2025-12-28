#!/usr/bin/env python3
# Python3 ile çalışacağını belirtir (ROS2 için standart)

import rclpy
# ROS2 Python client kütüphanesi

from rclpy.node import Node
# ROS2 Node sınıfı

from example_interfaces.msg import Int64
# 64 bit tam sayı mesaj tipi


class NumberPublisherNode(Node):
    # Sabit bir sayı yayınlayan publisher node sınıfı

    def __init__(self):
        # Node ilk oluşturulduğunda çalışır
        super().__init__("number_publisher")

        # number isimli topic için publisher oluşturulur
        self.publisher_ = self.create_publisher(
            Int64,
            "number",
            10
        )

        # Her 1 saniyede bir publish_number fonksiyonu çağrılır
        self.timer_ = self.create_timer(
            1.0,
            self.publish_number
        )

        # Publisher'ın başarıyla başlatıldığı bilgisi loglanır
        self.get_logger().info("Number publisher node başlatıldı.")

    def publish_number(self):
        # Int64 tipinde bir mesaj oluşturulur
        msg = Int64()

        # Yayınlanacak sayı mesaj içine atanır
        msg.data = 5

        # Mesaj topic üzerinden yayınlanır
        self.publisher_.publish(msg)


def main(args=None):
    # ROS2 sistemi başlatılır
    rclpy.init(args=args)

    # Publisher node oluşturulur
    node = NumberPublisherNode()

    # Node çalışmaya devam eder (timer burada çalışır)
    rclpy.spin(node)

    # ROS2 düzgün şekilde kapatılır
    rclpy.shutdown()


# Dosya doğrudan çalıştırıldığında main fonksiyonu çağrılır
if __name__ == "__main__":
    main()
