# first_ros2_pkg
My first package for ROS2

## Installation and Run nodes
```zsh 
$ cd ~/ros2_overlay_ws/src 
$ git clone https://github.com/ShotaAk/first_ros2_pkg

$ cd ..
$ colcon build

$ . ~/ros2_overlay_ws/install/local_setup.zsh
$ ros2 run first_python_pkg first_pub_node

# Launch new terminal
$ . ~/ros2_overlay_ws/install/setup.zsh
$ ros2 run first_cpp_pkg first_sub_node
```
