# Tutorial Workspace for Introduction to Robotics

In this workpsace we will create packages for the programming assignments.
You can start working on the first assignment immediatly.

## Assignment 1: Turtlesim

We will start by using the turtlesim simulation. You can find a lot of documentation for the turtlesim online, make sure that you read documentation for ros2 (version foxy-fitzroy).
Your task in this assignment is to enhance a 'watchdog' node, which intecepts and changes the inputs given by the user.

The goal of this assignment is that you familiarize with the ros2 ecosystem:
- launch a collection of nodes
- start individual nodes
- visualize topics and nodes using `rqt`
- see what messages are sent using `rqt` and `ros2 topic`
- modify existing code and see the effect of your changes
- learn to understand errors in your own code

To start you can install the workspace using `git clone`.
Build the workspace with the command `colcon build` (from the new directory you just downloaded). Now you have to 'source' the workspace `source install/setup.bash` to use it. You can also add this to your .bashrc file, so you do not have to do this every time you open a new terminal.

Start the package for assignment one in the following way:
- `ros2 launch watchdog watchdog.launch.py` will start the turtlesim and the watchdog node
- `ros2 run turtlesim turtle_teleop_key` starts the teleoperation node - this lets you steer the turtle
    - Use the arrow keys to turn the turtle (the keys GVBR etc. use another mechanism that controls the turtle which bypasses the watchdog node)
- Now you can inspect the current behaviour of the system with `rqt`
    - We suggest two plugins that you can enable: *introspection - node graph* and *topics - topic monitor*
- You can see that the teleop node directly steers the turtle - this is not what we want
    - You can redirect the output of the teleop node to the input topic for the watchdog node topic: `ros2 run turtlesim turtle_teleop_key --ros-args --remap turtle1/cmd_vel:=turtle1/input_cmd`
    - Check the changes in the node graph (the teleop node should now send its messages to the topic 'turtle1/input_cmd' which is subscribed by the watchdog)
    - Now the turtle should move backwards
- When the behaviour of the turtle is right, pay attention to the controller node
    - This node publishes a start and a stop message
    - Modify the behaviour of the watchdog, so the turtle is only able to turn before the start command is sent and stopped completly after the stop command is sent

## Assignment 2: Reactive Behaviour

Due date: May 3 / May 4 
In this assignment we want to program a reactive behaviour, that controls the robot by directly computing actuator commands from the sensor input. The sensor input we use is the laser scanner of the robot, which publishes to the `scan` topic. The velocity of the robot is controlled via the `cmd_vel` topic.

- Download the new code using git (you can either use a new branch for assigment 2, or merge the upstream changes to your local copy of the workspace).
- The new code is in a ros-package called `reactive_behaviour`, use `colcon build` and start the behaviour with `ros2 launch reactive_behaviour robot.launch.py n_robots:=1`
- You can modify the code within the file `controller.py` to change the behaviour of the robot
- Explore as much of the reachable area as possible (think of a cleaning robot)
- Don't crash ;)
# Introduction-to-Robotics-2022
# Introduction-to-Robotics-2022
