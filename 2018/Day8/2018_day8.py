"""
Read input file and do actions while reading line




"""
import numpy as np


def read_file(in_file):
    with open(in_file, 'r') as f:
        line = f.readline()
    return [int(i) for i in line.rstrip().split(' ')]


def recursive_node(inp_list):
    local_sum, child_node_list = 0, []
    node_value = inp_list.pop()
    runout_value = inp_list.pop()
    if node_value == 0:
        is_child = True
    else:
        is_child = False
    while node_value > 0:
        print(node_value, runout_value)
        recursive_call = recursive_node(inp_list)
        inp_list = recursive_call[0]
        child_node_list.append(recursive_call[1])
        node_value -= 1
    check_out_list = [inp_list.pop() for i in range(runout_value)]
    if is_child:
        local_sum += np.sum(check_out_list)
    else:
        local_sum += np.sum([child_node_list[cursor-1] for cursor in check_out_list if cursor-1 in range(len(child_node_list))])
    print(child_node_list, check_out_list, local_sum)
    return inp_list, local_sum


test_in = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
test_in_list = [int(i) for i in test_in.split(' ')]
test_in_list.reverse()
def main(input_list: list):
    input_list.reverse()
    checksum = 0
    while len(input_list) > 0:
        list_update = recursive_node(input_list)
        input_list = list_update[0]
        checksum += list_update[1]
        print(checksum)
    print(checksum)