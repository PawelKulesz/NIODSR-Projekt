import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        SetEnvironmentVariable(name='TURTLEBOT3_MODEL', value='burger'),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory('turtlebot3_gazebo'), 'launch', 'empty_world.launch.py')
            )
        ),
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