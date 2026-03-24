import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import math

class KinematicsSubscriber(Node):

    def __init__(self):
        super().__init__('kinematics_subscriber')
        self.subscription = self.create_subscription(
            JointState,
            'joint_states',
            self.listener_callback,
            10)
        
        self.L1 = 1.0
        self.L2 = 0.5
        self.L3 = 0.3

    def forward_kinematics(self, q1, q2, q3):

        px = (self.L2 * math.cos(q2) + self.L3 * math.cos(q2 + q3)) * math.cos(q1)
        py = (self.L2 * math.cos(q2) + self.L3 * math.cos(q2 + q3)) * math.sin(q1)
        pz = self.L1 - self.L2 * math.sin(q2) - self.L3 * math.sin(q2 + q3)
        
        return px, py, pz

    def listener_callback(self, msg):
        if len(msg.position) >= 3:
            q1, q2, q3 = msg.position[0], msg.position[1], msg.position[2]

            x, y, z = self.forward_kinematics(q1, q2, q3)

            self.get_logger().info(
                f'\n--- POSICIÓN ACTUAL ---\n'
                f'Ángulos: q1={q1:.2f}, q2={q2:.2f}, q3={q3:.2f}\n'
                f'Coordenadas: X={x:.3f}, Y={y:.3f}, Z={z:.3f}'
            )

def main(args=None):
    rclpy.init(args=args)
    node = KinematicsSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()