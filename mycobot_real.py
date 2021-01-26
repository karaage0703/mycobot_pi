import math
from mycobot_sim import NLinkArm
from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle

DEVICE_NAME = '/dev/tty.SLAB_USBtoUART'


def draw_robot():
    mycobot_sim.send_angles(mycobot_sim.convert_joint_angles_sim_to_mycobot(mycobot.get_radians()))
    mycobot_sim.forward_kinematics(plot=True)


def calc_ik(pos, plot=False):
    mycobot_sim.inverse_kinematics(pos, plot=plot)
    return mycobot_sim.convert_joint_angles_sim_to_mycobot(mycobot_sim.get_angles())


def move_robot(speed=50):
    mycobot.send_radians(mycobot_sim.convert_joint_angles_sim_to_mycobot(mycobot_sim.get_angles()), speed)


def move_initial_pose(speed=50):
    mycobot.send_angles([0.0, 0.0, 0.0, 0.0, 0.0, 0.0], speed)


mycobot = MyCobot(DEVICE_NAME)

mycobot_sim = NLinkArm([[0., math.pi / 2, 0, 0.13156],
                        [0., 0., -0.1104, 0.],
                        [0., 0., -0.096, 0.],
                        [0., math.pi / 2, 0., 0.06639],
                        [0., -math.pi / 2, 0., 0.07318],
                        [0., 0., 0., 0.0436]])
