import rclpy
from rclpy.node import Node
from rclpy.parameter import Parameter

class DyrosPyParam(Node):
    def __init__(self, node_name):
        super().__init__(node_name, allow_undeclared_parameters=True, automatically_declare_parameters_from_overrides=False)

        timer_period = 2
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.declare_parameter("name", "dyros")
        self.declare_parameters(
            namespace="gain",
            parameters=[('p', 100), ('i', 10), ('d', 1)]
        )
    
def main():
    node_name = "dyros_py_param_node"

    rclpy.init()
    param = DyrosPyParam(node_name)
    rclpy.spin(param)
    param.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()   
