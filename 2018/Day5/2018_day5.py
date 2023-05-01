###
import string
alpha_list = list(string.ascii_lowercase)


def read_file(in_file: str) -> str:
    out_str = ''
    with open(in_file, 'r') as f:
        for line in f.readlines():
            out_str += line
    return out_str


def opposite_case(inp: str) -> str:
    if inp.isupper():
        return inp.lower()
    else:
        return inp.upper()


in_file = '2018_day5_input.txt'
full_list = [char for char in read_file(in_file)]
for letter in alpha_list:
    poly_list = [char for char in full_list if char.lower() != letter]
    polymer_list = []
    test_val = poly_list.pop()
    while len(poly_list) > 0:
        next_val = poly_list.pop()
        if next_val == opposite_case(test_val):
            if len(polymer_list) == 0:
                test_val = poly_list.pop()
            else:
                test_val = polymer_list.pop()
        else:
            polymer_list.append(test_val)
            test_val = next_val
        if len(poly_list) == 0:
            polymer_list.append(test_val)
    print(letter, len(polymer_list))

