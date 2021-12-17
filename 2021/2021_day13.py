import re
import numpy as np
import string

def read_in_file(in_file):
    fold_list = []
    coord_list = []
    with open(in_file) as f:
        for line in f:
            line = line.rstrip()
            if line == '':
                continue
            elif line.startswith('fold'):
                input_value = line.split(' ')[-1].split('=')
                if input_value[0] == 'y':
                    input_value[0] = 1
                elif input_value[0] == 'x':
                    input_value[0] = 0
                else:
                    input_value[0] = 2
                input_value[1] = int(input_value[1])
                fold_list.append(input_value)
            elif line[0].isdigit():
                coord_list.append([int(i) for i in line.split(',')])
            else:
                continue
    return fold_list, coord_list

def build_array(coord_list):
    max_x = max([i[0] for i in coord_list]) + 1
    max_y = max([j[1] for j in coord_list]) + 1
    new_mat = np.zeros([max_y, max_x], dtype=int)

    for j in coord_list:
        new_mat[j[1]][j[0]] = 1

    return new_mat


def fold(inp_array, ax: int, pivot: int):
    final_array = np.copy(inp_array)
    if pivot == 0 or pivot == inp_array.shape[1] - 1:
        final_array = np.delete(final_array, ax, pivot - 1)
    elif ax == 0:
        arr_midpoint = final_array.shape[1]/2
        left_array = final_array[:, :pivot]
        right_array = final_array[:, pivot+1:]
        if pivot >= arr_midpoint:
            for i in range(right_array.shape[1]):
                left_array[:, -1-i] += right_array[:, i]
            final_array = left_array
        else:
            for j in range(left_array.shape[1]):
                right_array[:, j] += left_array[:, left_array.shape[1]-1-j]
            final_array = right_array
    elif ax == 1:
        arr_midpoint = final_array.shape[0]/2
        top_array = final_array[:pivot, :]
        bottom_array = final_array[pivot+1:, :]
        if pivot <= arr_midpoint:
            for i in range(bottom_array.shape[0]):
                top_array[-1-i, :] += bottom_array[i, :]
            final_array = top_array
        else:
            for j in range(top_array.shape[0]):
                bottom_array[j, :] += top_array[top_array.shape[0]-1-j, :]
            final_array = bottom_array
    else:
        return ValueError()
    print(final_array.shape)
    print(final_array)
    return final_array
"""
[[0 1 1 0 0 0 0 1 1 0 0 1 0 0 1 0 0 0 0 1 0 1 0 0 1 0 1 1 0 0 0 1 1 1 1 0 0 1 1 0]
 [0 1 0 0 0 0 1 0 0 1 0 1 0 0 1 0 0 0 0 1 0 0 1 0 1 0 1 0 0 0 0 0 0 0 1 0 1 0 0 1]
 [0 1 0 0 0 0 0 0 0 1 0 1 0 0 1 0 0 0 0 1 0 0 0 1 1 0 1 0 0 0 0 0 1 1 1 0 0 0 0 1]
 [0 1 0 0 0 0 1 1 0 1 0 1 0 0 1 0 0 0 0 1 0 0 1 0 1 0 1 0 0 0 0 0 0 0 1 0 0 0 0 1]
 [0 1 0 0 1 0 1 0 0 1 0 1 0 0 1 0 0 0 0 1 0 0 1 0 1 0 1 0 0 1 0 0 0 0 1 0 1 0 0 1]
 [0 0 1 1 0 0 1 1 1 0 0 0 1 1 0 0 1 1 1 1 0 1 0 0 1 0 0 1 1 0 0 1 1 1 1 0 0 1 1 0]]
 
 [[0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
  [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
  [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
  [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0],
  [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0],
  [0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0]]
        C           E                 J             K               L               U              G               J
"""