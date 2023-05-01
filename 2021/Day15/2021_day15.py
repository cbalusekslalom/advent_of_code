import numpy as np
def read_in_file(in_file):
    list_of_lists = []
    with open(in_file, 'r') as f:
        for line in f.readlines():
            list_of_lists.append([int(char) for char in line.rstrip()])
    return np.array(list_of_lists)

start_point = [0,0]
end_point = new_map.shape[0], new_map.shape[1]
visited_list = []

def visit_once(inp_array, node, visited_list):
    res = []
    new_visit = visited_list + [node]
    if node == (inp_array.shape[0], inp_array.shape[1]):
        return [new_visit]
    for n in inp_array[node]:
        if n != 'start':
            if n not in visited_list or n.isupper():
                temp_res = visit_once(graph_dict, n, new_visit)
                res.extend(temp_res)
    return res

def node_choice(inp_array, node, visited_list):
    res = []
    new_visit = visited_list + [node]

def dijkstra(graph, source):
    