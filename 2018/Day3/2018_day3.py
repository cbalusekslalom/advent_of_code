""""""
import os
from collections import defaultdict

## tuple generator
## store into dictionary for each claim
## compare all keys in dict to lok at values that overlap

## 0 index, 1st is l/r, 2nd is t/b, 1st is width, 2nd is height


def tuple_list_generator(input_string) -> list:
    tuple_list = []
    start_pt, size = input_string.split(':')[0], input_string.split(':')[1].lstrip()
    x_pos, y_pos = int(start_pt.split(',')[0]), int(start_pt.split(',')[1])
    width, height = int(size.split('x')[0]), int(size.split('x')[1])
    for w in range(width):
        for h in range(height):
            tuple_list.append((x_pos+w, y_pos+h))
    return tuple_list


def main(in_file):
    m = defaultdict(list)
    with open(in_file) as f:
        for line in f.readlines():
            ## #1 @ 896,863: 29x19
            key_val= line.split('@')[0]
            value_to_process = tuple_list_generator(line.split('@')[1])


            intersection += [coordinate for coordinate in value_list if coordinate in union]
            union += [coordinate for coordinate in value_list if coordinate not in union]
        print(f"finished with line {counter}.  Total intersections: {len(intersection)}.")
        del value_list


if __name__ == "__main__":
    main(os.path.join(os.getcwd(), '2018_day3_input.txt'))