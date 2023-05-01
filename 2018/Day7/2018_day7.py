"""
Making a graph
"""
import re
import numpy as np
import string
alphabet = string.ascii_uppercase


def read_input(in_file: str):
    graph = {}
    for letter in alphabet:
        graph[letter] = []
    with open(in_file, 'r') as f:
        for line in f.readlines():
            regex_list = [i for i in re.split(r"Step (\w{1}) must be finished before step (\w{1}) can begin.", line) if i != '']
            graph[regex_list[0]].append(regex_list[1])
    for key in graph.keys():
        graph[key].sort()
    return graph


def check_empty_list(dict_obj: dict) -> dict:
    pop_list = []
    for key in dict_obj.keys():
        if dict_obj[key] == []:
            pop_list.append(key)
    return pop_list


def rem_val(dict_obj: dict, val) -> dict:
    for key, value in dict_obj.items():
        if val in value:
            dict_obj[key].remove(val)
    return dict_obj


def main(input_file):
    new_graph = read_input(input_file)
    key_len = np.sum([1 for key in new_graph.keys()])
    string_order = []
    while key_len > 0:
        end_points_values = check_empty_list(new_graph)
        end_points_values.sort(reverse=True)
        for val in end_points_values:
            new_graph.pop(val)
            string_order.append(val)
            new_graph = rem_val(new_graph, val)
        key_len = np.sum([1 for key in new_graph.keys()])
    print(string_order)
    # rev_list.append(val)