#!/usr/bin/env python3
# Dosyanın Python3 ile çalışacağını belirtir

import rclpy
# ROS2 Python istemci kütüphanesi

from rclpy.node import Node
# ROS2 Node sınıfı

from example_interfaces.msg import String
# String mesaj tipi


class RobotStatePublisherNode(Node):
    # Robotun durum bilgisini yayınlayan node

    def __init__(self):
        # Node oluşturulduğunda çalışır
        super().__init__("robot_state_publisher")

        # Robotun ismi (sabit bilgi)
        self.robot_name = "Rover-001"

        # state_publisher topic'i için String tipinde publisher oluşturulur
        self.publisher_ = self.create_publisher(
            String,
            "state_publisher",
            10
        )

        # Her 0.5 saniyede bir publish_state fonksiyonu çağrılır
        self.timer_ = self.create_timer(
            0.5,
            self.publish_state
        )

        # Node'un başarıyla başlatıldığı loglanır
        self.get_logger().info("Robot durum yayınlayıcı başlatıldı.")


    def publish_state(self):
        # String tipinde bir mesaj oluşturulur
        msg = String()

        # Robotun durum mesajı hazırlanır
        msg.data = f"Hello this is {self.robot_name} from Konya Yolu!"

        # Mesaj topic üzerinden yayınlanır
        self.publisher_.publish(msg)


def main(args=None):
    # ROS2 sistemi başlatılır
    rclpy.init(args=args)

    # Publisher node oluşturulur
    node = RobotStatePublisherNode()

    # Node sürekli çalışır (timer burada aktif olur)
    rclpy.spin(node)

    # ROS2 düzgün şekilde kapatılır
    rclpy.shutdown()


# Dosya doğrudan çalıştırıldığında main fonksiyonu çağrılır
if __name__ == "__main__":
    main()
