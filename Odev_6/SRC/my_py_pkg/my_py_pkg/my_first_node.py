#!/usr/bin/env python3
# Python3 ile çalışacağını belirtir (ROS2 için standart)

import rclpy
# ROS2 Python client kütüphanesi

from rclpy.node import Node
# ROS2 Node sınıfı


class MyNode(Node):
    # Basit bir ROS2 Python node sınıfı

    def __init__(self):
        # Node ilk oluşturulduğunda çalışır
        super().__init__("python_test")

        # Sayaç değişkeni başlatılır
        self.counter_ = 0

        # Node başladığında bilgilendirme mesajı yazdırılır
        self.get_logger().info("Merhaba ROS2")

        # Her 0.5 saniyede bir timer_callback fonksiyonu çağrılır
        self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        # Sayaç değeri 1 artırılır
        self.counter_ += 1

        # Güncel sayaç değeri ekrana yazdırılır
        self.get_logger().info(f"Hello {self.counter_}")


def main(args=None):
    # ROS2 sistemi başlatılır
    rclpy.init(args=args)

    # Node oluşturulur
    node = MyNode()

    # Node çalışmaya devam eder (timer burada çalışır)
    rclpy.spin(node)

    # ROS2 düzgün şekilde kapatılır
    rclpy.shutdown()


# Dosya doğrudan çalıştırıldığında main fonksiyonu çağrılır
if __name__ == "__main__":
    main()
