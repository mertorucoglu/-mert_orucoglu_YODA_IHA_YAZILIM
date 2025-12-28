#!/usr/bin/env python3
# Python3 ile çalışacağını belirtir (ROS2 için standart)

import rclpy
# ROS2 Python client kütüphanesi

from rclpy.node import Node
# ROS2 Node sınıfı


class TemplateNode(Node):  # TODO: Rename
    # ROS2 node şablonu (template)
    # TODO: Rename → Bu sınıf adı, node’un yapacağı işe göre değiştirilmelidir

    def __init__(self):
        # Node ilk oluşturulduğunda çalışır
        super().__init__("template_node")  # TODO: Rename
        # TODO: Rename → ROS2 ağı üzerinde görünen node adı,
        #                projenin amacına göre değiştirilmelidir


def main(args=None):
    # ROS2 sistemi başlatılır
    rclpy.init(args=args)

    # TemplateNode tipinde bir node oluşturulur
    node = TemplateNode()  # TODO: Rename
    # TODO: Rename → Eğer sınıf adı değişirse burada da güncellenmelidir

    # Node çalışmaya devam eder
    rclpy.spin(node)

    # ROS2 düzgün şekilde kapatılır
    rclpy.shutdown()


# Dosya doğrudan çalıştırıldığında main fonksiyonu çağrılır
if __name__ == "__main__":
    main()