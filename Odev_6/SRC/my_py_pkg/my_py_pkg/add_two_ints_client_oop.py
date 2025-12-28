#!/usr/bin/env python3
# Python3 ile çalışacağını belirtir (ROS2 için standart)

import rclpy
# ROS2 Python client kütüphanesi

from rclpy.node import Node
# ROS2 Node sınıfı

from example_interfaces.srv import AddTwoInts
# İki tamsayıyı toplayan servis tanımı

from functools import partial
# Callback fonksiyonuna ekstra parametre göndermek için kullanılır


class AddTwoIntsClientNode(Node):
    # AddTwoInts servisini çağıran client node sınıfı

    def __init__(self):
        # Node ilk oluşturulduğunda çalışır
        super().__init__("add_two_ints_client")

        # Node başlatılır başlatılmaz üç farklı servis çağrısı yapılır
        self.call_add_two_ints_client(5, 6)
        self.call_add_two_ints_client(5, 16)
        self.call_add_two_ints_client(15, 63)

    def call_add_two_ints_client(self, a, b):
        # add_two_ints servisinde client oluşturulur
        client = self.create_client(AddTwoInts, "add_two_ints")

        # Servis hazır olana kadar beklenir
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Servis bekleniyor: add_two_ints")

        # Servise gönderilecek istek nesnesi oluşturulur
        request = AddTwoInts.Request()

        # Toplanacak ilk sayı
        request.a = a

        # Toplanacak ikinci sayı
        request.b = b

        # Servis asenkron olarak çağrılır
        future = client.call_async(request)

        # Servis yanıtı geldiğinde çalışacak callback fonksiyonu tanımlanır
        # partial ile a ve b değerleri callback içine taşınır
        future.add_done_callback(
            partial(self.callback_call_add_two_ints, a=a, b=b)
        )

    def callback_call_add_two_ints(self, future, a, b):
        # Servisten yanıt geldiğinde otomatik olarak çalışır
        try:
            # Servisten dönen yanıt alınır
            response = future.result()

            # Toplama sonucu ekrana yazdırılır
            self.get_logger().info(f"{a} + {b} = {response.sum}")

        except Exception as e:
            # Servis çağrısı sırasında hata oluşursa yakalanır
            self.get_logger().error("Servis çağrısı başarısız oldu! %r" % (e,))


def main(args=None):
    # ROS2 sistemi başlatılır
    rclpy.init(args=args)

    # Client node oluşturulur
    node = AddTwoIntsClientNode()

    # Node çalışmaya devam eder (callback’ler burada işlenir)
    rclpy.spin(node)

    # ROS2 düzgün şekilde kapatılır
    rclpy.shutdown()


# Dosya doğrudan çalıştırıldığında main fonksiyonu çağrılır
if __name__ == "__main__":
    main()
