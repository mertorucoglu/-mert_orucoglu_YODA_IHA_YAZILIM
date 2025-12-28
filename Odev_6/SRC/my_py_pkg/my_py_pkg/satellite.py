#!/usr/bin/env python3
# Dosyanın Python3 ile çalışacağını belirtir

import rclpy
# ROS2 Python istemci kütüphanesi

from rclpy.node import Node
# ROS2 Node sınıfı

from example_interfaces.msg import String
# String mesaj tipi


class SatelliteNode(Node):
    # Robotun yayınladığı durum mesajlarını dinleyen uydu (subscriber) node

    def __init__(self):
        # Node oluşturulduğunda çalışır
        super().__init__("satellite")

        # state_publisher topic'ine subscriber oluşturulur
        # Mesaj tipi: String
        # Gelen mesajlar callback_satellite fonksiyonuna yönlendirilir
        self.subscriber_ = self.create_subscription(
            String,
            "state_publisher",
            self.callback_satellite,
            10
        )

        # Subscriber node'un başlatıldığı bilgisi loglanır
        self.get_logger().info("Satellite node başlatıldı.")

    def callback_satellite(self, msg):
        # state_publisher topic'inden yeni mesaj geldiğinde çalışır
        # Gelen mesajın içeriği ekrana yazdırılır
        self.get_logger().info(msg.data)


def main(args=None):
    # ROS2 sistemi başlatılır
    rclpy.init(args=args)

    # Subscriber node oluşturulur
    node = SatelliteNode()

    # Node çalışmaya devam eder ve mesajları dinler
    rclpy.spin(node)

    # ROS2 düzgün şekilde kapatılır
    rclpy.shutdown()


# Dosya doğrudan çalıştırıldığında main fonksiyonu çağrılır
if __name__ == "__main__":
    main()
