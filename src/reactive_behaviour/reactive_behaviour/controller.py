import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class VelocityController(Node):

    def __init__(self):
        super().__init__('velocity_controller')
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.forward_distance = 0
        self.left_distance = 0
        self.right_distance = 0
        self.create_subscription(LaserScan, 'scan', self.laser_cb, rclpy.qos.qos_profile_sensor_data)
        self.create_timer(0.1, self.timer_cb)
        self.get_logger().info('controller node started')
        
        
    def timer_cb(self):
        msg = Twist()
        x = self.forward_distance - 0.3
        x = x if x < 0.1 else 0.1
        x = x if x >= 0 else 0.0
        msg.linear.x = x
        
        #Turtle ist direkt vor Wand
        if (x==0):
            msg.angular.z = msg.angular.z - 0.5 #nach rechts drehen
        
        #Turtle ist links zu nah an einer Wand
        left = self.left_distance - 0.3
        if left < 0.1:
            msg.angular.z = msg.angular.z - 0.5 #leicht nach rechts drehen
        
        #Turtle ist rechts zu nah an einer Wand
        right = self.right_distance - 0.3
        if right < 0.1:
            msg.angular.z = msg.angular.z + 0.5 #leicht nach links drehen
        
        self.publisher.publish(msg)
    
    def laser_cb(self, msg):
        self.forward_distance = msg.ranges[0]
        self.left_distance = msg.ranges[89]
        self.right_distance = msg.ranges[269]
        #self.get_logger().info(f'left: {msg.ranges[269]}')



def main(args=None):
    rclpy.init(args=args)

    node = VelocityController()

    rclpy.spin(node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
