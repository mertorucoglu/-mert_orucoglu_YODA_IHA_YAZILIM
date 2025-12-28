#!/usr/bin/env python3
# Python3 ile çalışacağını belirtir (ROS2 için standart)

import rclpy
# ROS2 Python client kütüphanesi

from rclpy.node import Node
# Node sınıfını kullanabilmek için içe aktarılır

from example_interfaces.srv import AddTwoInts
# İki tamsayıyı toplayan hazır servis tanımı


def main(args=None):
    # ROS2 sistemini başlatır
    rclpy.init(args=args)

    # "add_two_ints_client_node" isimli bir node oluşturulur
    node = Node("add_two_ints_client_node")

    # add_two_ints servisinde AddTwoInts tipinde bir client oluşturulur
    client = node.create_client(AddTwoInts, "add_two_ints")

    # Servis beklenir
    while not client.wait_for_service(1.0):
        node.get_logger().warn("Servis bekleniyor...")

    # Servise gönderilecek istek nesnesi oluşturulur
    request = AddTwoInts.Request()

    # Toplanacak ilk sayı
    request.a = 5

    # Toplanacak ikinci sayı
    request.b = 14

    # Servis  çağrılır
    future = client.call_async(request)

    # Servisten yanıt gelene kadar node çalışır
    rclpy.spin_until_future_complete(node, future)

    try:
        # Servisten gelen yanıt alınır
        response = future.result()

        # Toplama sonucu ekrana yazdırılır
        node.get_logger().info(f"{request.a} + {request.b} = {response.sum}")

    except Exception as e:
        # Servis çağrısı sırasında hata oluşursa yakalanır
        node.get_logger().error("Servis çağrısı başarısız oldu! %r" % (e,))

    # ROS2 düzgün şekilde kapatılır
    rclpy.shutdown()


# Dosya doğrudan çalıştırıldığında main fonksiyonu çağrılır
if __name__ == "__main__":
    main()
