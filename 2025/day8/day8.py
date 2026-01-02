import os
from collections import defaultdict
import numpy as np
import operator
from functools import reduce

def read_file(inTxt):
    file_name = os.path.join(os.getcwd(), '2025/inputs/'+inTxt)
    three_dim_dict = {}
    counter = 0
    with open(file_name, 'r') as f:
        for line in f.readlines():
            if counter not in three_dim_dict.keys():
                three_dim_dict[counter] = [int(inp) for inp in line.strip().split(',')]
            counter += 1
    return three_dim_dict 

def calc_distance(in1, in2):
    return float(np.sqrt(reduce(operator.add, [(i-j)**2 for i,j in zip(in1, in2)])))

def get_key_of_min_value(d):
    if not d:  # Handle empty dictionary case
        return None
    return min(d, key=d.get)

def nearest_neighbor(input_dict):
    circuit_dict = {k:0 for k in input_dict}
    for key in input_dict.keys():
        min_key = get_key_of_min_value(input_dict[key])
        circuit_dict[key] = (min_key, input_dict[min_key][key])
    return circuit_dict

def reverse_dict(input_dict):
    reverse = {k:[] for k in input_dict.values()}
    for k, v in input_dict.items():
        reverse[v].append(k)
    return reverse

def build_circuit(input_dict):
    # start with a key
    # we get each of the values
    # we get the keys that have a value of myself or the value of my value
    # for each key that has my value or my values value they extend the list
    list_of_lists = []
    key_list = []
    for key in input_dict.keys():
        if key in key_list:
            continue

        outList = [key]
        print(key)
        if key not in key_list:
            key_list.append(key)
            next_key = input_dict[key]
            if next_key in key_list:
                for l in list_of_lists:
                    if next_key in l and not key in l:
                        l.append(key)
            print(next_key)
            while not next_key in key_list:
                key_list.append(next_key)
                outList.append(next_key)
                next_key = input_dict[next_key]
            list_of_lists.append(outList)
        print(key_list)
    return list_of_lists

def main(inTxt, iter):
    dim_dict = read_file(inTxt)
    tuple_list = [[i,j] for i in dim_dict.keys() for j in dim_dict.keys() if i != j and i < j]
    closest_neighbor_dict = {calc_distance(dim_dict[tpl[0]], dim_dict[tpl[1]]):(tpl[0], tpl[1]) for tpl in tuple_list}
    neighbor = nearest_neighbor(closest_neighbor_dict)
    step = 0
    list_of_connections = []
    key_list = [key for key in closest_neighbor_dict.keys()]
    while step < iter:
        for key, value in neighbor.items():
            value[1] 


        if key_value in l for l in list_of_connections:
            l.append(key_value)
        iter+=1
    
    circuit_start = build_circuit(neightbor)
    print(circuit_start)


                
        
