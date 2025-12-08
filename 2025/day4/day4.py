import os,sys 
import numpy as np

def make_array(inTxt):
    with open(os.path.join(os.getcwd(), '2025/inputs/' +inTxt), 'r') as f:
        list_of_lists = [[i for i in line.strip()] for line in f.readlines()]
    return np.array(list_of_lists)

def check_symbol(element, symbol):
    if element == symbol:
        return 1
    return 0

def tuple_list(input_tpl: tuple) -> list[tuple]:
    # take in the array shape and return a list of all tuples
    return [(i,j) for i in range(0,input_tpl[0]) for j in range(0,input_tpl[1])]


def check_pos(input_tpl, array_map):
    x_pos, y_pos = input_tpl[0], input_tpl[1]
    #print(array_map[x_pos][y_pos])
    count = 0
    sign = array_map[x_pos][y_pos]
    if sign == '.':
        return None
    for pos_x in range((x_pos-1),(x_pos+2)):
        if pos_x<0:
            count += 0
            continue
        if pos_x>=array_map.shape[0]:
            count+= 0
            continue
        for pos_y in range((y_pos-1),(y_pos+2)):
            if pos_y < 0: 
                count += 0
                continue 
            if pos_y >= array_map.shape[1]: 
                count += 0
                continue 
            #print(f"The character in position {pos_x}, {pos_y} is {array_map[pos_x][pos_y]}")
            if pos_x == x_pos and pos_y == y_pos:
                count += 0
                continue
            if array_map[pos_x][pos_y] == '@':
                count += 1
    if count < 4:
        return (x_pos, y_pos)
    return None

def update_tuple(tpl_list, array_map):
    for tpl in tpl_list:
        print(tpl)
        array_map[tpl[0]][tpl[1]] = '.'
    return array_map

def main(inTxt):
    counter = 0
    array_of_bales = make_array(inTxt)
    list_of_tuples = tuple_list(array_of_bales.shape)
    total_bales = [check_pos(tpl, array_of_bales) for tpl in list_of_tuples if check_pos(tpl, array_of_bales)]
    bales_to_move = len(total_bales)
    grand_total_moved = bales_to_move
    while bales_to_move > 0:
        print(f"iteration {counter}")
        counter += 1
        temp_array = update_tuple(total_bales, array_of_bales)
        total_bales = [check_pos(tpl, temp_array) for tpl in list_of_tuples if check_pos(tpl, temp_array)]
        bales_to_move = len(total_bales)
        grand_total_moved += bales_to_move
        array_of_bales = temp_array
    print(grand_total_moved, counter)
    return total_bales

if __name__ == '__main__':
    main('day4.txt')
