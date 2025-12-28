#!/usr/bin/env python3
# Python3 ile çalışacağını belirtir (ROS2 için standart)

import rclpy
# ROS2 Python client kütüphanesi

from rclpy.node import Node
# ROS2 Node sınıfı

from example_interfaces.msg import Int64
# 64 bit tam sayı mesaj tipi

from example_interfaces.srv import SetBool
# Boolean değer alan servis tanımı


class NumberCounterNode(Node):
    # Gelen sayıları toplayan ve sonucu yayınlayan node sınıfı

    def __init__(self):
        # Node ilk oluşturulduğunda çalışır
        super().__init__("number_counter")

        # Toplamı tutan sayaç değişkeni
        self.counter_ = 0

        # number_count topic'i için publisher oluşturulur
        self.number_publisher_ = self.create_publisher(
            Int64,
            "number_count",
            10
        )

        # number topic'ini dinleyen subscriber oluşturulur
        self.subscriber_ = self.create_subscription(
            Int64,
            "number",
            self.callback_number_count,
            10
        )

        # reset_counter isimli servis oluşturulur
        self.reset_counter_service_ = self.create_service(
            SetBool,
            "reset_counter",
            self.callback_reset_counter
        )

        # Node'un başarıyla başlatıldığı bilgisi loglanır
        self.get_l_
