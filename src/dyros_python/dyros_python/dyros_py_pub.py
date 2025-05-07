import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class DyrosPyPublisher(Node):
    def __init__(self, node_name, topic_name):
        super().__init__(self, node_name, topic_name)
        self.publisher_ = self.create_publisher(Int32, topic_name, 10)
        timer_period = 1.0
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Int32()
        msg.data = self.i
        self.publisher_.publish(msg)
        self.get_logger().info("Publishing: %d " % msg.data)
        self.i += 1

def main(args=None):
        rclpy.init(args=args)

        node_name = "dyros_pu_pub_node"
        topic_name = "dyros_pub_sub_topic"

        pub = DyrosPyPublisher(node_name, topic_name)

        rclpy.spin(pub)

        pub.destroy_node()
        rclpy.shutdown()


if __name__=="__main__":
    main()