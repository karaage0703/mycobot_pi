import pygame.midi
from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle

pygame.init()
pygame.midi.init()

DEVICE_NAME = '/dev/tty.SLAB_USBtoUART'
mycobot = MyCobot(DEVICE_NAME)

if __name__ == '__main__':
    for i in range(pygame.midi.get_count()):
        interf, name, input_dev, output_dev, opened = pygame.midi.get_device_info(i)
        if input_dev and b'X-TOUCH MINI' in name:
            print('X-TOUCH MINI is found, midi id=' + str(i))
            midi_input = pygame.midi.Input(i)

    joint_angles = [0, 0, 0, 0, 0, 0]
    while True:
        if midi_input.poll():
            midi_events = midi_input.read(10)
            joint_numb = midi_events[0][0][1]
            joint_angle = midi_events[0][0][2]
            if joint_numb < 7:
                joint_angles[joint_numb - 1] = joint_angle
                print(joint_angles)
                mycobot.send_angles(joint_angles, 50)
