# Moonbot software

Simulation based for slam and navigation test on mobile robot

## Prerequisties
* Ubuntu 22.04
* ros2-humble

## Installation
* Installation of ros2-humblee: [https://docs.ros.org/en/humble/Installation/Alternatives/Ubuntu-Development-Setup.html](), and source the ros2 package in the terminal.
```bash
source /opt/ros/humble/setup.bash
```

* Install dependencies
```bash
sudo apt-get update

rosdep install --from-paths src --ignore-src -r -y

sudo apt install joystick

sudo apt install ros-humble-joy* ros-humble-teleop*

sudo apt instal ros-humble-twist-stamper

sudo apt install ros-humble-navigation2

sudo apt install ros-humble-nav2-bringup

sudo apt instal ros-humble-twist-mux


```

* Install program
```bash
cd ros2_ws/

colcon build --symlink-install

source install/setup.bash
```


## Packages description 
### rover_description
- URDF and mesh files for robots
- RVIZ configuration.
- Launch file for visualizing the robot model in RVIZ

```bash
# For changing robot model
ros2 launch moonbot_description rsp.launch.py urdf_file:=your_robot.urdf
```

### rover_gazebo
- Model and world files for Gazebo simulation. 
- Launch file to spawn robot in Gazebo

World files and robot model are also changable by the following commands
```bash
# For changing world file (The example for obstables map)
ros2 launch rover_gazebo spawn_rover.launch.py world_file_name:=obstacles.world
```

### rover_navigation
- Navigation params for Nav2

Nav2 with AMCL (Launch the simulation first)
```bash
# terminal 1
ros2 launch rover_navigation localization_launch.py map:=your_map_file.yaml use_sim_time:=true

# terminal 2
ros2 launch rover_navigation navigation_launch.py use_sim_time:=true map_subscribe_transient_local:=true 
```

To send a navigation goal through the command line
```bash
# With an action server
ros2 action send_goal /navigate_to_pose nav2_msgs/action/NavigateToPose "pose: {header: {frame_id: map}, pose: {position: {x: 1.52, y: 1.92, z: 0.0}, orientation:{x: 0.0, y: 0.0, z: 0, w: 1.0000000}}}"

# With a topic
ros2 topic pub -1 /goal_pose geometry_msgs/PoseStamped "{header: {stamp: {sec: 0}, frame_id: 'map'}, pose: {position: {x: 2.2, y: 0.0, z: 0.0}, orientation: {w: 1.0}}}"
```


## Author
Tharit Sinsunthorn
