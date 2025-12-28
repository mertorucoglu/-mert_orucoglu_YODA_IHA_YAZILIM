#!/usr/bin/env python3
# Python3 ile çalışacak ROS2 node dosyası

import rclpy
# ROS2 Python istemci kütüphanesi

from rclpy.node import Node
# ROS2 Node sınıfı

from geometry_msgs.msg import Twist
# Turtle'ın lineer ve açısal hızlarını kontrol eden mesaj tipi


class TurtleSpiral(Node):
    # Turtle'ın spiral şeklinde hareket etmesini sağlayan node

    def __init__(self):
        # Node oluşturulduğunda çalışır
        super().__init__('turtle_spiral_node')

        # /turtle1/cmd_vel topic'i için publisher oluşturulur
        # Twist mesajı ile hız komutları gönderilir
        self.publisher_ = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10
        )
        
        # Her 0.5 saniyede bir timer_callback fonksiyonu çağrılır
        self.timer = self.create_timer(
            0.5,
            self.timer_callback
        )
        
        # İleri hızın zamanla artırılması için sayaç değişkeni
        self.speed_counter = 0.0
        
        # Node'un çalışmaya başladığı bilgisi
        self.get_logger().info('Turtle spiral hareket node başlatıldı.')

    def timer_callback(self):
        # Timer tetiklendiğinde çalışır
        msg = Twist()
        
        # Spiral hareket mantığı:
        # - Açısal hız (angular.z) sabit tutulur
        # - Lineer hız (linear.x) her adımda artırılır
        # Bu sayede turtle dairesel değil, spiral bir yol çizer
        
        self.speed_counter += 0.2  # İleri hız kademeli olarak artırılır
        
        msg.linear.x = self.speed_counter  # Artan ileri hız
        msg.angular.z = 2.0                # Sabit dönüş hızı
        
        # Hesaplanan hız komutu turtle'a gönderilir
        self.publisher_.publish(msg)
        
        # Gönderilen hız bilgisi terminale yazdırılır
        self.get_logger().info(
            f"Gönderilen hız -> İleri: {msg.linear.x:.1f}, Dönüş: {msg.angular.z}"
        )


def main(args=None):
    # ROS2 sistemi başlatılır
    rclpy.init(args=args)

    # TurtleSpiral node oluşturulur
    node = TurtleSpiral()
    
    try:
        # Node çalışmaya devam eder
        rclpy.spin(node)
    except KeyboardInterrupt:
        # CTRL+C ile çıkıldığında hata oluşmaması için
        pass
    finally:
        # Node ve ROS2 düzgün şekilde kapatılır
        node.destroy_node()
        rclpy.shutdown()


# Dosya doğrudan çalıştırıldığında main fonksiyonu çağrılır
if __name__ == '__main__':
    main()