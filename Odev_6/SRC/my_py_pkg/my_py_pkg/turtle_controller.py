#!/usr/bin/env python3
# Python3 ile çalışacak ROS2 node dosyası

import rclpy
# ROS2 Python istemci kütüphanesi

from rclpy.node import Node
# ROS2 Node sınıfı

from geometry_msgs.msg import Twist
# Turtle'ı hareket ettirmek için kullanılan hız mesajı

from turtlesim.msg import Pose
# Turtle'ın konum bilgisini içeren mesaj tipi


class TurtleBouncer(Node):
    # Turtle'ın duvarlara çarpmadan hareket etmesini sağlayan node

    def __init__(self):
        # Node oluşturulduğunda çalışır
        super().__init__('turtle_bouncer_node')
        
        # Turtle'a hız komutu gönderen publisher
        # /turtle1/cmd_vel topic'i üzerinden Twist mesajı yayınlar
        self.cmd_vel_publisher_ = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10
        )
        
        # Turtle'ın anlık konum bilgisini dinleyen subscriber
        # /turtle1/pose topic'inden Pose mesajı alır
        self.pose_subscriber_ = self.create_subscription(
            Pose, 
            '/turtle1/pose', 
            self.pose_callback, 
            10
        )
        
        # Node'un çalışmaya başladığı bilgisi
        self.get_logger().info('Turtle bouncer node başlatıldı.')

    def pose_callback(self, pose: Pose):
        # Turtle'ın konumu her güncellendiğinde çalışır
        cmd = Twist()
        
        # Güvenli hareket alanı: x ve y için 2.0 - 9.0 arası
        # Turtle bu sınırların dışına yaklaşırsa yön değiştirir
        
        if (
            pose.x > 9.0 or pose.x < 2.0 or
            pose.y > 9.0 or pose.y < 2.0
        ):
            # Turtle duvara yaklaşıyor
            cmd.linear.x = 1.0     # İleri hız azaltılır
            cmd.angular.z = 0.9    # Dönerek yön değiştirir
        else:
            # Turtle güvenli alan içinde
            cmd.linear.x = 5.0     # Sabit hızla ileri gider
            cmd.angular.z = 0.0    # Düz hareket eder
            
        # Hesaplanan hız komutu turtle'a gönderilir
        self.cmd_vel_publisher_.publish(cmd)


def main(args=None):
    # ROS2 sistemi başlatılır
    rclpy.init(args=args)

    # TurtleBouncer node oluşturulur
    node = TurtleBouncer()

    # Node sürekli çalışır ve pose verisini dinler
    rclpy.spin(node)

    # Node düzgün şekilde kapatılır
    node.destroy_node()
    rclpy.shutdown()


# Dosya doğrudan çalıştırıldığında main fonksiyonu çağrılır
if __name__ == '__main__':
    main()
