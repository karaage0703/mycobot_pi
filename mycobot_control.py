import argparse
import serial
import time

HEADER = 'FA'
FOOTER = 'FE'
BAUDRATE = 115200

parser = argparse.ArgumentParser(description='mycobot_control')

parser.add_argument('serial_name', help='serial name')

args = parser.parse_args()

ser = serial.Serial(args.serial_name, BAUDRATE, timeout=0.1)
time.sleep(1)


def set_rgb(rgb):
    """Set the light color

    Args:
        rgb (str): example 'ff0000' # red
    """

    command = HEADER + HEADER + '05' + '33' + rgb + FOOTER
    ser.write(bytes.fromhex(command))


def set_angle(servo_no, angle, speed):
    """Set the robot angle

    Args:
        servo_no (str): '01' to '06'
        angle (int): -180 to 180
        speed (str): '0000' to ?
    """

    ANGLE_TO_ENCODER = 11.3777777
    ENCODER_CAL_POINT = 2048

    if angle > 180:
        angle = 180

    if angle < -180:
        angle = -180

    servo_encoder_value = int(angle * ANGLE_TO_ENCODER) + ENCODER_CAL_POINT
    servo_encoder_value = '%04X' % servo_encoder_value

    command = (
        HEADER + HEADER + '07' + '20' +
        servo_no + servo_encoder_value[2:4] + servo_encoder_value[0:2] +
        speed[2:4] + speed[0:2] + FOOTER)
    ser.write(bytes.fromhex(command))
