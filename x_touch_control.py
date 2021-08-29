import pygame.midi
from pymycobot.mycobot import MyCobot
# from pymycobot.genre import Angle
import copy

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

    midi_control_enable = [False, False, False, False, False, False,
                           False, False, False, False, False, False]
    joint_angles = [0, 0, 0, 0, 0, 0]
    mycobot.send_angles(joint_angles, 10)
    print('Please press key after robot motion is stopped.')
    input()
    base_coords = mycobot.get_coords()
    new_coords = copy.copy(base_coords)
    print('Current joint angles')
    print(mycobot.get_angles())
    print('Current coordination')
    print(base_coords)

    while True:
        if midi_input.poll():
            midi_events = midi_input.read(10)
            print(midi_events)
            midi_control_channel = midi_events[0][0][1]
            midi_control_value = midi_events[0][0][2]
            if midi_control_channel < 7:
                if midi_control_enable[midi_control_channel - 1]:
                    joint_angles[midi_control_channel - 1] = (midi_control_value - 64) * 2.8
                    mycobot.send_angles(joint_angles, 50)
                else:
                    if midi_control_value == 64:
                        midi_control_enable[midi_control_channel - 1] = True

            if 10 < midi_control_channel < 17:
                coords_numb = midi_control_channel - 11
                if midi_control_enable[midi_control_channel - 5]:
                    if coords_numb == 2:
                        new_coords[coords_numb] = base_coords[coords_numb] + (midi_control_value - 127) * 1.0
                    else:
                        new_coords[coords_numb] = base_coords[coords_numb] + (midi_control_value - 64) * 1.0
                    mycobot.send_coords(new_coords, 30, 0)
                else:
                    if coords_numb == 2:
                        if midi_control_value == 127:
                            midi_control_enable[midi_control_channel - 5] = True
                    else:
                        if midi_control_value == 64:
                            midi_control_enable[midi_control_channel - 5] = True

            if midi_control_channel == 8 or midi_control_channel == 32:
                mycobot.set_color(0, 0, 0)
            if midi_control_channel == 9 or midi_control_channel == 33:
                mycobot.set_color(255, 0, 0)
            if midi_control_channel == 10 or midi_control_channel == 34:
                mycobot.set_color(0, 255, 0)
            if midi_control_channel == 11 or midi_control_channel == 35:
                mycobot.set_color(0, 0, 255)
