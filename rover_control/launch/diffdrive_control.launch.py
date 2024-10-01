import random

from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import ExecuteProcess, IncludeLaunchDescription, RegisterEventHandler
from launch.event_handlers import OnProcessExit, OnProcessStart
from launch.launch_description_sources import PythonLaunchDescriptionSource

# this is the function launch  system will look for


def generate_launch_description():

    joint_state_broadcaster_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_state_broadcaster",
                   "--controller-manager", "/controller_manager"],
    )

    robot_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["diff_cont", "-c", "/controller_manager"],
    )

    # create and return launch description object
    return LaunchDescription(
        [
            # RegisterEventHandler(
            #     event_handler=OnProcessExit(
            #       target_action=spawn_robot,
            #       on_exit=[joint_state_broadcaster_spawner],
            #     )
            # ),
            joint_state_broadcaster_spawner,
            
            RegisterEventHandler(
                event_handler=OnProcessExit(
                  target_action=joint_state_broadcaster_spawner,
                  on_exit=[robot_controller_spawner],
                )
            ),
        ]
    )