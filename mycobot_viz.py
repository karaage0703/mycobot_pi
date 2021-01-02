import math
from vizualization import NLinkArm
from mycobot3 import MyCobot

DEVICE_NAME = '/dev/tty.SLAB_USBtoUART'


def convert_joint_angles_sim_to_mycobot(joint_angles):
    conv_mul = [-1.0, -1.0, 1.0, -1.0, -1.0, -1.0]
    conv_add = [0.0, -math.pi / 2, 0.0, -math.pi / 2, math.pi / 2, 0.0]

    joint_angles = [joint_angles * conv_mul for (joint_angles, conv_mul) in zip(joint_angles, conv_mul)]
    joint_angles = [joint_angles + conv_add for (joint_angles, conv_add) in zip(joint_angles, conv_add)]

    joint_angles_lim = []
    for joint_angle in joint_angles:
        while joint_angle > math.pi:
            joint_angle -= 2 * math.pi

        while joint_angle < -math.pi:
            joint_angle += 2 * math.pi

        joint_angles_lim.append(joint_angle)

    return joint_angles_lim


def draw_robot():
    mycobot_sim.send_angles(convert_joint_angles_sim_to_mycobot(mycobot.get_angles_of_radian()))
    mycobot_sim.forward_kinematics(plot=True)


def calc_ik(pos, plot=False):
    mycobot_sim.inverse_kinematics(pos, plot=plot)
    return convert_joint_angles_sim_to_mycobot(mycobot_sim.get_angles())


def move_robot(pose, speed=50):
    mycobot.send_angles_by_radian(convert_joint_angles_sim_to_mycobot(mycobot_sim.get_angles()), speed)


def move_initial_pose(speed=50):
    mycobot.send_angles([0.0, 0.0, 0.0, 0.0, 0.0, 0.0], speed)


mycobot = MyCobot(DEVICE_NAME)

mycobot_sim = NLinkArm([[0., math.pi / 2, 0, 0.13156],
                        [0., 0., -0.1104, 0.],
                        [0., 0., -0.096, 0.],
                        [0., math.pi / 2, 0., 0.06639],
                        [0., -math.pi / 2, 0., 0.07318],
                        [0., 0., 0., 0.0436]])
