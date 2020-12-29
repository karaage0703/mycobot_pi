import argparse
import serial
import time

BAUDRATE = 115200

HEADER = 'FA'
FOOTER = 'FE'

ANGLE_TO_ENCODER = 11.3777777
ENCODER_CAL_POINT = 2048

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


def _convert_servo_encoder_value(angle):
    """Convert angle(degree) to servo encoder value

    Args:
        angle (int): -180 to 180 (degree)

    Returns:
        str: servo encoder value
    """

    ANGLE_TO_ENCODER = 11.3777777
    ENCODER_CAL_POINT = 2048

    if angle > 180:
        angle = 180

    if angle < -180:
        angle = -180

    servo_encoder_value = int(angle * ANGLE_TO_ENCODER) + ENCODER_CAL_POINT
    servo_encoder_value = '%04X' % servo_encoder_value

    return servo_encoder_value


def set_angle(servo_no, angle, speed):
    """Set the robot angle

    Args:
        servo_no (str): '01' to '06'
        angle (int): -180 to 180 (degree)
        speed (str): '0000' to ?
    """

    servo_encoder_value = _convert_servo_encoder_value(angle)

    command = (
        HEADER + HEADER + '07' + '20' +
        servo_no + servo_encoder_value[2:4] + servo_encoder_value[0:2] +
        speed[2:4] + speed[0:2] + FOOTER)

    ser.write(bytes.fromhex(command))


def set_angles(angles, speed):
    """Set the robot angle

    Args:
        angles (list): example[10, 180, -30, 0, 10, 20] (degree)
        speed (str): '0000' to ?
    """

    if len(angles) != 6:
        raise Exception('Error!')
    else:
        servo_encoder_values = []
        for angle in angles:
            servo_encoder_values.append(_convert_servo_encoder_value(angle))

        command = HEADER + HEADER + '10' + '21'
        for servo_encoder_value in servo_encoder_values:
            command += servo_encoder_value[2:4] + servo_encoder_value[0:2]
        command += speed[2:4] + speed[0:2] + FOOTER

        ser.write(bytes.fromhex(command))


# Test commands:
# python -i mycobot_control.py '/dev/tty.SLAB_USBtoUART'
# >>> set_rgb('FF0000') # red
# >>> set_angle('01', 0, '0005')
# >>> set_angle('04', 0, '0005')
# set_angles([0,10,200,-180,-200,0], '0005')
