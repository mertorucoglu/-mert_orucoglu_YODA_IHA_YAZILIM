#!/usr/bin/env python3
# Python3 ile çalışacağını belirtir (ROS2 için standart)

import rclpy
# ROS2 Python client kütüphanesi

from rclpy.node import Node
# ROS2 Node sınıfı

from my_custom_interfaces.msg import DeviceStatus
# Custom olarak oluşturulmuş DeviceStatus mesaj tipi


class DeviceStatusPublisherNode(Node):
    # Cihaz durumunu yayınlayan (publisher) node sınıfı

    def __init__(self):
        # Node ilk oluşturulduğunda çalışır
        super().__init__("device_status_publisher")

        # device_status isimli topic için publisher oluşturulur
        self.status_publisher_ = self.create_publisher(
            DeviceStatus,
            "device_status",
            10
        )

        # Her 1 saniyede bir publish_device_status fonksiyonu çağrılır
        self.timer_ = self.create_timer(
            1.0,
            self.publish_device_status
        )

        # Publisher'ın başarıyla başlatıldığı bilgisi loglanır
        self.get_logger().info("Cihaz durumu yayınlayıcı başlatıldı.")

    def publish_device_status(self):
        # DeviceStatus tipinde bir mesaj oluşturulur
        msg = DeviceStatus()

        # Motor hızı bilgisi atanır
        msg.motor_speed = 75

        # Sensörün açık olduğu bilgisi a
