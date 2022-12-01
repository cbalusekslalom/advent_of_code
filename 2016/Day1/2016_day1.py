import os
import sys
import numpy as np


def read_input(path):
    with open(path) as f:
        out = f.readline().split(', ')
    return out


instructions = read_input("/Users/curtis.balusek/Documents/Training/aoc/2016/inputs/2016_day1_input.txt")


def direction(inp_list):
    bearing = 0 ## 0 is N, 90 is E, 180 is S, 270 is W, 360 or 0 is N.
    start_pos = (0, 0)
    position_list = [(0, 0)]
    for inp in inp_list:
        distance = int(inp[1:])
        if inp[0] == 'R':
            bearing = (bearing + 90) % 360
        else:
            bearing = (bearing - 90) % 360
        if bearing == 0:
            start_pos = (start_pos[0], start_pos[1] + distance)
        elif bearing == 90:
            start_pos = (start_pos[0] + distance, start_pos[1])
        elif bearing == 180:
            start_pos = (start_pos[0], start_pos[1] - distance)
        elif bearing == 270:
            start_pos = (start_pos[0] - distance, start_pos[1])
        else:
            print('error with input')
        print(bearing, start_pos)
        if start_pos not in position_list:
            position_list.append(start_pos)
        else:
            print(np.abs(start_pos[0]) + np.abs(start_pos[1]))
            break
    print(np.abs(start_pos[0]) + np.abs(start_pos[1]))







