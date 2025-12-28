#!/usr/bin/env python3
# Python3 ile çalışacağını belirtir (ROS2 için standart)

import rclpy
# ROS2 Python client kütüphanesi

from rclpy.node import Node
# ROS2 Node sınıfı

from example_interfaces.srv import AddTwoInts
# İki tamsayıyı toplayan servis tanımı


class AddTwoIntsServer(Node):
    # AddTwoInts servisini sağlayan (server) node sınıfı

    def __init__(self):
        # Node ilk oluşturulduğunda çalışır
        super().__init__("add_two_ints_server_node")

        # add_two_ints isimli servis oluşturulur
        # Servis çağrıldığında callback_add_two_ints fonksiyonu çalışır
        self.server_ = self.create_service(
            AddTwoInts,
            "add_two_ints",
            self.callback_add_two_ints
        )

        # Servisin başarıyla başlatıldığı loglanır
        self.get_logger().info("Add Two Ints servisi başlatıldı.")

    def callback_add_two_ints(self, request, response):
        # Client tarafından gönderilen iki sayı toplanır
        response.sum = request.a + request.b

        # Yapılan işlem ekrana yazdırılır
        self.get_logger().info(f"{request.a} + {request.b} = {response.sum}")

        # Hesaplanan yanıt client'a geri gönderilir
        return response


def main(args=None):
    # ROS2 sistemi başlatılır
    rclpy.init(args=args)

    # Servis node'u oluşturulur
    node = AddTwoIntsServer()

    # Node sürekli çalışır ve servis çağrılarını bekler
    rclpy.spin(node)

    # ROS2 düzgün şekilde kapatılır
    rclpy.shutdown()


# Dosya doğrudan çalıştırıldığında main fonksiyonu çağrılır
if __name__ == "__main__":
    main()
