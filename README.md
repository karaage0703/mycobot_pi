# mycobot_pi
Python script of myCobot

![](./docs/images/robot_sim.png)

![](./docs/images/robot_real.jpg)

## Dependency

- Python3
- macOS / Linux
- Numpy
- Matplotlib
- myCobot Atom version 2.4
- pymycobot==2.1.2

## Setup

Execute following commands:

```sh
$ pip3 install pymycobot==2.1.2
$ git clone https://github.com/karaage0703/mycobot_pi
$ cd mycobot_pi
```

## Usage

```python
$ python3 -i mycobot_viz.py 
>>> move_initial_pose(speed=50)
>>> draw_robot()
>>> joint_angles = calc_ik([0.15, 0.2, 0.1, 0, 0, 0], plot=True)
>>> move_robot(speed=50)
>>> move_initial_pose()
>>> move_robot(speed=80)
>>> move_initial_pose(speed=80)
```

## License

This software is released under the MIT License, see LICENSE.

## References

- https://github.com/elephantrobotics/myCobot
- https://github.com/AtsushiSakai/PythonRobotics
