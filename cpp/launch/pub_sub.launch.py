
from launch import LaunchDescription

import launch.actions
import launch_ros.actions


def generate_launch_description():
    return LaunchDescription([
        launch.actions.LogInfo(
            msg="launch publisher node and subscriber node"),

        launch.actions.TimerAction(period=5.0,actions=[
            launch.actions.LogInfo(
                msg="----------This is a TimerAction!!!---------"),
            ]),

        launch_ros.actions.Node(
            package='first_python_pkg',
            node_executable='first_pub_node',
            output='screen'),

        launch_ros.actions.Node(
            package='first_cpp_pkg',
            node_executable='first_sub_node',
            output='screen'),
        ])
