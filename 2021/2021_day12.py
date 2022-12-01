
def read_in_file(in_file):
    graph_dict = {}
    with open(in_file, 'r') as f:
        for line in f.readlines():
            newline = line.rstrip().split('-')
            print(newline)
            left = newline[0]
            right = newline[1]
            print(left, right)
            if left not in graph_dict:
                graph_dict[left] = [right]
            else:
                graph_dict[left].append(right)
            if right not in graph_dict:
                graph_dict[right] = [left]
            else:
                graph_dict[right].append(left)
    return graph_dict


def new_key_dict(in_graph):
    key_dict = {}
    for key in in_graph.keys():
        if key.isupper():
            key_dict[key] = 2
        else:
            key_dict[key] = 1
    return key_dict


def visit_once(graph_dict, node, visited_list):
    res = []
    new_visit = visited_list + [node]
    if node == 'end':
        return [new_visit]
    for n in graph_dict[node]:
        if n != 'start':
            if n not in visited_list or n.isupper():
                temp_res = visit_once(graph_dict, n, new_visit)
                res.extend(temp_res)
    return res

new_graph = read_in_file('2021_day12_input.txt')
visited_list = [[]]

print(new_graph.keys())

