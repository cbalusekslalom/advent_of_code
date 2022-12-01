"""
Read in input and generate array
check all right facing
check all down facing
count number of ones where objects move


[['v' '.' '.' '.' '>' '>' '.' 'v' 'v' '>']
 ['.' 'v' 'v' '>' '>' '.' 'v' 'v' '.' '.']
 ['>' '>' '.' '>' 'v' '>' '.' '.' '.' 'v']
 ['>' '>' 'v' '>' '>' '.' '>' '.' 'v' '.']
 ['v' '>' 'v' '.' 'v' 'v' '.' 'v' '.' '.']
 ['>' '.' '>' '>' '.' '.' 'v' '.' '.' '.']
 ['.' 'v' 'v' '.' '.' '>' '.' '>' 'v' '.']
 ['v' '.' 'v' '.' '.' '>' '>' 'v' '.' 'v']
 ['.' '.' '.' '.' 'v' '.' '.' 'v' '.' '>']]
 #########################################
[['v' '.' '.' '.' '>' '.' '>' 'v' 'v' '>']
 ['.' 'v' 'v' '>' '.' '>' 'v' 'v' '.' '.']
 ['>' '.' '>' '>' 'v' '.' '>' '.' '.' 'v']
 ['>' '>' 'v' '>' '.' '>' '.' '>' 'v' '.']
 ['v' '>' 'v' '.' 'v' 'v' '.' 'v' '.' '.']
 ['.' '>' '>' '.' '>' '.' 'v' '.' '.' '.']
 ['.' 'v' 'v' '.' '.' '.' '>' '>' 'v' '.']
 ['v' '.' 'v' '.' '.' '>' '>' 'v' '.' 'v']
 ['>' '.' '.' '.' 'v' '.' '.' 'v' '.' '.']]
  #########################################
[['.' '.' '.' '.' '>' '.' '>' 'v' '.' '>']
 ['v' '.' 'v' '>' '.' '>' 'v' '.' 'v' '.']
 ['>' 'v' '>' '>' '.' '.' '>' 'v' '.' '.']
 ['>' '>' 'v' '>' 'v' '>' '.' '>' '.' 'v']
 ['.' '>' 'v' '.' 'v' '.' '.' '.' 'v' '.']
 ['v' '>' '>' '.' '>' 'v' 'v' 'v' '.' '.']
 ['.' '.' 'v' '.' '.' '.' '>' '>' '.' '.']
 ['v' 'v' '.' '.' '.' '>' '>' 'v' 'v' '.']
 ['>' '.' 'v' '.' 'v' '.' '.' 'v' '.' 'v']]


"""
import numpy as np


def read_in_file(in_file):
    list_of_lists = []
    with open(in_file, 'r') as file:
        for line in file.readlines():
            list_of_lists.append([char for char in line.rstrip()])
    return np.array((list_of_lists), dtype=str)


def check_next_space(direction, inp_array, i, j):
    if direction == '>':
        if i == inp_array.shape[0]:
            next_ind_x = 0
        else:
            next_ind_x = i + 1
        next_space = inp_array[next_ind_x][j]
    elif direction == 'v':
        if j == inp_array.shape[1]:
            next_ind_y = 0
        else:
            next_ind_y = j + 1
        next_space = inp_array[i][next_ind_y]
    else:
        ValueError


inp_array = read_in_file('2021_day25_test.txt')

inp_array = read_in_file('2021_day25_input.txt')
# check '>'
step = 0
move_counter = 1
while move_counter > 0:
    move_counter = 0
    step += 1
    update_array = np.zeros((inp_array.shape[0], inp_array.shape[1]), dtype=str)
    for i in range(inp_array.shape[0]):
        for j in range(inp_array.shape[1]):
            if inp_array[i, j] == '>':
                # row i, column j for moving right, look at j+1
                next_check = [0 if j == inp_array.shape[1]-1 else j + 1][0]
                # print(f"curr_pos: {i, j} new pos: {i, next_check}")
                if inp_array[i, next_check] == '.':
                    update_array[i, next_check] = '>'
                    update_array[i, j] = '.'
                    move_counter += 1
                else:
                    continue
    for i in range(update_array.shape[0]):
        for j in range(update_array.shape[1]):
            if update_array[i, j] == '>':
                inp_array[i, j] = '>'
            elif update_array[i, j] == '.':
                inp_array[i, j] = '.'
            else:
                continue
    update_array = np.zeros((inp_array.shape[0], inp_array.shape[1]), dtype=str)
    # check 'v'
    for k in range(inp_array.shape[0]):
        for m in range(inp_array.shape[1]):
            if inp_array[k, m] == 'v':
                # row i, column j for moving right, look at j+1
                next_check = [0 if k == inp_array.shape[0]-1 else k + 1][0]
                next_spot = inp_array[next_check, m]
                if inp_array[next_check, m] == '.':
                    update_array[next_check, m] = 'v'
                    update_array[k, m] = '.'
                    move_counter += 1
                else:
                    continue
    for i in range(update_array.shape[0]):
        for j in range(update_array.shape[1]):
            if update_array[i, j] == 'v':
                inp_array[i, j] = 'v'
            elif update_array[i, j] == '.':
                inp_array[i, j] = '.'
            else:
                continue
    print(f"step: {step} and move_counter: {move_counter}")


