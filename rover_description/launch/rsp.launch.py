import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.conditions import IfCondition

import xacro


def generate_launch_description():

    ####### DATA INPUT ##########
    # urdf_file = 'moonbotX.urdf'
    package_description = "rover_description"
    
    use_sim_time = LaunchConfiguration('use_sim_time')
    
    use_joint_state_gui = LaunchConfiguration('use_joint_state_gui')
    
    # robot_file = LaunchConfiguration('robot_file')
    
    # xacro_path = LaunchConfiguration('xacro_path')

    # Process the URDF file
    pkg_path = os.path.join(get_package_share_directory(package_description))
    
    # robot_file_arg = DeclareLaunchArgument(
    #     'robot_file',
    #     default_value='rover.urdf.xacro'
    # )
    
    # xacro_file_arg = DeclareLaunchArgument(
    #     'xacro_path',
    #     default_value=[os.path.join(pkg_path,'urdf', 'hero_3ws', 'moonbot_hero.xacro')]
    # )
    
    xacro_file = os.path.join(pkg_path,'urdf', 'rover.urdf.xacro')
    
    robot_description_config = xacro.process_file(xacro_file)
    
    gui_arg = DeclareLaunchArgument(
        'use_joint_state_gui',
        default_value='True'
    )
    
    # Create a robot_state_publisher node
    params = {'robot_description': robot_description_config.toxml(), 'use_sim_time': use_sim_time}
    
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[params]
    )
    
    
    # RVIZ Configuration
    rviz_config_dir = os.path.join(
        get_package_share_directory(package_description), 
        'rviz', 
        'rover_rviz.rviz'
    )
    
    # Joint State Publisher
    joint_state_publisher_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        output='screen',
        condition=IfCondition(use_joint_state_gui)
    )
    
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        output='screen',
        name='rviz_node',
        parameters=[{'use_sim_time': True}],
        arguments=['-d', rviz_config_dir]
    )


    # Launch!
    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use sim time if true'),

        gui_arg,
        # robot_file_arg,
        # xacro_file_arg,
        robot_state_publisher_node,
        joint_state_publisher_node,
        rviz_node
    ])