# mycobot_pi
Python script of myCobot

![](./docs/images/robot_sim.png)

![](./docs/images/robot_real.jpg)

## Dependency

- Python3
- macOS / Linux
- Numpy
- Matplotlib

## Setup

Execute following commands:

```sh
$ git clone https://github.com/karaage0703/mycobot_pi
$ cd mycobot_pi
$ wget https://raw.githubusercontent.com/elephantrobotics/myCobot/main/API/Python/pymycobot/mycobot3.py
```

## Usage

```python
$ python3 -i mycobot_viz.py 
>>> move_initial_pose(speed=50)
>>> draw_robot()
>>> joint_angles = calc_ik([0.15, 0.2, 0.1, 0, 0, 0], plot=True)
>>> move_robot(joint_angles, speed=50)
>>> move_initial_pose()
>>> move_robot(joint_angles, speed=80)
>>> move_initial_pose(speed=80)
```

## License

This software is released under the MIT License, see LICENSE.

## References

- https://github.com/elephantrobotics/myCobot
- https://github.com/AtsushiSakai/PythonRobotics
