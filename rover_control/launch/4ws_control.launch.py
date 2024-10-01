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

    steering_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["forward_position_controller", "-c", "/controller_manager"],
    )
    
    wheel_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["forward_velocity_controller", "-c", "/controller_manager"],
    )
    
    leg1_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["leg1position_trajectory_controller", "-c", "/controller_manager"],
    )
    
    leg2_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["leg2position_trajectory_controller", "-c", "/controller_manager"],
    )
    
    leg3_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["leg3position_trajectory_controller", "-c", "/controller_manager"],
    )
    
    leg4_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["leg4position_trajectory_controller", "-c", "/controller_manager"],
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
            
            wheel_controller_spawner,
            steering_controller_spawner,
            # leg1_controller_spawner,
            # leg2_controller_spawner,
            # leg3_controller_spawner,
            # leg4_controller_spawner
            
        ]
    )