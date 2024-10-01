# SRL ros2 control workshop

Simulation based for slam and navigation test on mobile robot

## Prerequisties
* Ubuntu 22.04
* ros2-humble

## Installation
* Installation of ros2-humble: [https://docs.ros.org/en/humble/Installation/Alternatives/Ubuntu-Development-Setup.html](), and source the ros2 package in the terminal.
```bash
source /opt/ros/humble/setup.bash
```

* Install dependencies
```bash
sudo apt-get update

rosdep install --from-paths src --ignore-src -r -y

sudo apt install joystick

sudo apt install ros-humble-joy* ros-humble-teleop*

sudo apt install ros-humble-twist-stamper

sudo apt install ros-humble-twist-mux


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

```bash
# For using teleop control via key board)
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args --remap cmd_vel:=diff_cont/cmd_vel_unstamped

```

### rover_control
- Config file for controllers
- Launch file for ros2 controller manager

### rover_teleop 
- Launch and joy stick related files


## Author
Tharit Sinsunthorn
