from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='camera_subscriber',
            executable='camera_node',
            name='camera_node',
            output='screen',
            parameters=[
                {'square_size': 200}
            ]
        ),
        Node(
            package='camera_subscriber',
            executable='turtle_controller',
            name='turtle_controller',
            output='screen'
        ),
    ])