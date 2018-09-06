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

## Launch nodes
```zsh
$ ros2 launch first_cpp_pkg pub_sub.launch.py
[INFO] [launch.user]: launch publisher node and subscriber node
[INFO] [launch]: process[first_pub_node-1]: started with pid [828]
[INFO] [launch]: process[first_sub_node-2]: started with pid [829]
[INFO] [first_pub_node]: Publishing: "Hello World! ^^: 0"
[INFO] [first_sub_node]: I heard: 'Hello World! ^^: 0'
[INFO] [first_pub_node]: Publishing: "Hello World! ^^: 1"
[INFO] [first_sub_node]: I heard: 'Hello World! ^^: 1'
[INFO] [first_pub_node]: Publishing: "Hello World! ^^: 2"
[INFO] [first_sub_node]: I heard: 'Hello World! ^^: 2'
[INFO] [first_pub_node]: Publishing: "Hello World! ^^: 3"
[INFO] [first_sub_node]: I heard: 'Hello World! ^^: 3'
[INFO] [first_pub_node]: Publishing: "Hello World! ^^: 4"
[INFO] [first_sub_node]: I heard: 'Hello World! ^^: 4'
[INFO] [first_pub_node]: Publishing: "Hello World! ^^: 5"
[INFO] [first_sub_node]: I heard: 'Hello World! ^^: 5'
[INFO] [first_pub_node]: Publishing: "Hello World! ^^: 6"
[INFO] [first_sub_node]: I heard: 'Hello World! ^^: 6'
[INFO] [first_pub_node]: Publishing: "Hello World! ^^: 7"
[INFO] [first_sub_node]: I heard: 'Hello World! ^^: 7'
[INFO] [first_pub_node]: Publishing: "Hello World! ^^: 8"
[INFO] [first_sub_node]: I heard: 'Hello World! ^^: 8'
[INFO] [launch.user]: ----------This is a TimerAction!!!---------
[INFO] [first_pub_node]: Publishing: "Hello World! ^^: 9"
[INFO] [first_sub_node]: I heard: 'Hello World! ^^: 9'
[INFO] [first_pub_node]: Publishing: "Hello World! ^^: 10"
[INFO] [first_sub_node]: I heard: 'Hello World! ^^: 10'
```
