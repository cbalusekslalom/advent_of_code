import numpy as np
from contextlib import suppress

def read_file(in_file):
    new_array = []
    with open(in_file) as f:
        for line in f.readlines():
            new_array.append([int(num) for num in line.rstrip()])
    return np.array(new_array)

def array_checking(inp_array):
    min_arr = np.full(inp_array.shape, 0, dtype=int)
    for (x, y), value in np.ndenumerate(inp_array):
        keep_flag = True
        #check left
        if x >= 0:
            if inp_array[x-1, y] <= value:
                keep_flag = False
                continue
        #check right
        with suppress(IndexError):
            if inp_array[x+1, y] <= value:
                keep_flag = False
                continue
        #check top
        with suppress(IndexError):
            if inp_array[x,y-1] <= value:
                keep_flag = False
                continue
        #check bottom
            if inp_array[x, y+1] <= value:
                keep_flag = False
                continue

        if keep_flag:
            min_arr[x, y] = value+1
        else:
            min_arr[x, y] = 0
    return min_arr


def list_subtraction(list_in: list, list_sub: list):
    out_list = []
    for j in range(min(len(list_in),len(list_sub))):
        out_list.append(list_in[j] - list_sub[j])
    return out_list


def array_area(inp_array):
    boundary_array = np.where(inp_array == np.amax(inp_array), 1, 0)
    coord_list, value_list = [], []
    area_list, count = [], 0
    for (x, y), value in np.ndenumerate(boundary_array):
        coord_list.append([x,y])
        value_list.append(value)
    ones_list = [i for i, j in enumerate(value_list) if j == 1]
    ones_list.reverse()
    for ind in ones_list:
        coord_list.pop(ind)
        value_list.pop(ind)
    while len(coord_list) > 1:
        count += 1
        start_coord = coord_list.pop(0)
        print(start_coord)
        check_coor, area_coors = [start_coord], [start_coord]
        while len(check_coor) > 0:
            iterate_coor = check_coor.pop()
            # Check left
            left_position = list_subtraction(iterate_coor, [-1, 0])
            if left_position in coord_list:
                check_coor.append(left_position)
                area_coors.append(left_position)
                coord_list.remove(left_position)
            #check top
            top_position = list_subtraction(iterate_coor, [0, -1])
            if top_position in coord_list:
                check_coor.append(top_position)
                area_coors.append(top_position)
                coord_list.remove(top_position)
            #check right
            right_position = list_subtraction(iterate_coor, [1, 0])
            if right_position in coord_list:
                check_coor.append(right_position)
                area_coors.append(right_position)
                coord_list.remove(right_position)
            #check bottom
            bottom_position = list_subtraction(iterate_coor, [0, 1])
            if bottom_position in coord_list:
                check_coor.append(bottom_position)
                area_coors.append(bottom_position)
                coord_list.remove(bottom_position)

        # End of inner where clause
        print(f"for {start_coord}, registered {area_coors}.")
        area_list.append(len(area_coors))
        print(f'completed number {count}')
    return  area_list
    # end of outer where clause



    keep_flag = True
    #check left
    if x >= 0:
        if inp_array[x-1, y] <= value:
            keep_flag = False
            continue
    #check right
    with suppress(IndexError):
        if inp_array[x+1, y] <= value:
            keep_flag = False
            continue
    #check top
    with suppress(IndexError):
        if inp_array[x,y-1] <= value:
            keep_flag = False
            continue
        #check bottom
        if inp_array[x, y+1] <= value:
            keep_flag = False
            continue

    if keep_flag:
        min_arr[x, y] = value+1
    else:
        min_arr[x, y] = 0
    return min_arr


### Check corners
### Check edges
### check middle