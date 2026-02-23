import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class Publicador_Numeros(Node):

    def __init__(self):
        super().__init__('publicador')
        self.publisher_ = self.create_publisher(String, 'FrancoM', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.migen = self.numeros_primos()

    def timer_callback(self):
        msg = String()
        siguiente_primo = next(self.migen)
        msg.data = str(siguiente_primo)
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

    def es_primo(self,n):
    
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def numeros_primos(self):
        numero = 2
        while True:
            if self.es_primo(numero):
                yield numero  
            numero += 1

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = Publicador_Numeros()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()