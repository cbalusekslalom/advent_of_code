"""
Insert for polymers
"""


def read_in_file(in_file):
    poly_dic, ref_dict = {}, {}
    with open(in_file, 'r') as f:
        start_polymer = [char for char in f.readline().rstrip()]
        f.readline()
        for line in f.readlines():
            line_out = line.rstrip().split(" -> ")
            ref_dict[line_out[0]] = line_out[1]
    return start_polymer, ref_dict
    #return polymer, ref_dict


def append_input(inp_list, inp_dict):
    start = inp_list.pop(0)
    new_out_list = [start]
    while len(inp_list) > 0:
        second = inp_list.pop(0)
        key = start + second
        new_out_list.append(inp_dict[key])
        start = second
        new_out_list.append(start)
    return new_out_list


def map_dic(inp_ref):
    left_gen, right_gen = {}, {}
    for key, val in inp_ref.items():
        left_gen[key] = key[0] + val
        right_gen[key] = val + key[1]
    return left_gen, right_gen


def iterate_dict(input_dict, inp_ref):
    out_dict = {item: 0 for item in inp_ref}
    l, r = map_dic(inp_ref)
    for key, value in input_dict.items():
        left_key = l[key]
        right_key = r[key]
        out_dict[left_key] += value
        out_dict[right_key] += value
    return out_dict


def make_element_list(ref_dict):
    letter_list = []
    for i in ref_dict.keys():
        if i[0] not in letter_list:
            letter_list.append(i[0])
        if i[1] not in letter_list:
            letter_list.append(i[1])
    return letter_list

## random factor of 2????
def main(in_file, n):
    polymer, ref = read_in_file(in_file)
    element_list = make_element_list(ref)
    poly_dic = {item: 0 for item in ref}
    element = {item: 0 for item in element_list}

    for i in range(1, len(polymer)):
        new_key = polymer[i-1] + polymer[i]
        poly_dic[new_key] += 1
    print(polymer, '\n', poly_dic)

    for i in range(n):
        poly_dic = iterate_dict(poly_dic, ref)

    for key, value in poly_dic.items():
        element[key[0]] += poly_dic[key]
        element[key[1]] += poly_dic[key]
    print(poly_dic, element)
    return element
