"""
Read input file
Only consider files with x1=x2 or y1=y2
For each set of line segments : update matrix.
Start at 0, find max value for matrix
Create matrix of 0s

"""
import numpy as np
import matplotlib.pyplot as plt

def make_matrix(n: int):
    return [[0] * n for ind in range(n)]


def weird_division(a, b):
    return a / b if b else 0


class Vent:
    """Create a vent Object for mapping inputs"""

    def __init__(self, n: int):
        self.size = n
        self.matrix = make_matrix(n)
        self.danger_zones = 0

    def update_segment(self, inp_tup, inp_tup_2):
        x1, y1 = int(inp_tup[0]), int(inp_tup[1])
        x2, y2 = int(inp_tup_2[0]), int(inp_tup_2[1])
        check_slope = weird_division((y2 - y1), (x2 - x1))
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2)+1):
                self.matrix[i][x1] += 1
        elif y1 == y2:
            for j in range(min(x1, x2), max(x1, x2)+1):
                self.matrix[y1][j] += 1
        elif check_slope == 1:
            for k, m in zip(range(min(y1, y2), max(y1, y2) + 1), range(min(x1, x2), max(x1, x2) + 1)):
                self.matrix[k][m] += 1
        elif check_slope == -1:
            for y, z in zip(range(min(y1, y2), max(y1, y2) + 1), range(max(x1, x2), min(x1, x2) - 1, -1)):
                self.matrix[y][z] += 1
        else:
            print(f'skipping {inp_tup, inp_tup_2} for not matching conditions')
            pass

    def print_matrix(self):
        for s in self.matrix:
            print(*s)

    def count_dangers(self):
        self.danger_zones = sum([1 for row in self.matrix for i in row if i > 1])
        print(f" There are {self.danger_zones} danger zones")


def read_input_file(in_text: str):
    output_list = []
    with open(in_text, 'r') as f:
        for line in f.readlines():
            output_list.append([i.split(',') for i in line.strip().split(' -> ')])
    return output_list


def main(inp_file: str, n: int):
    input_segments = read_input_file(inp_file)
    new_vent = Vent(n)
    for inp_seg in input_segments:
        new_vent.update_segment(inp_seg[0], inp_seg[1])
    new_vent.count_dangers()

    H = np.array(new_vent.matrix)

    fig = plt.figure(figsize=(8, 8))

    ax = fig.add_subplot(111)
    ax.set_title('colorMap')
    plt.imshow(H)
    ax.set_aspect('equal')
    plt.show()

    #cax = fig.add_axes([0.12, 0.1, 0.78, 0.8])
    cax.get_xaxis().set_visible(False)
    cax.get_yaxis().set_visible(False)
    cax.patch.set_alpha(0)
    cax.set_frame_on(False)
    plt.colorbar(orientation='vertical')
    plt.show()


def update_segment(inp_matrix, inp_tup, inp_tup_2):
    x1, y1 = int(inp_tup[0]), int(inp_tup[1])
    x2, y2 = int(inp_tup_2[0]), int(inp_tup_2[1])
    check_slope = weird_division((y2 - y1), (x2 - x1))
    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2)+1):
            inp_matrix[i][x1] += 1
    elif y1 == y2:
        for j in range(min(x1, x2), max(x1, x2)+1):
            inp_matrix[y1][j] += 1
    elif check_slope == 1:
        for i, j in zip(range(min(y1, y2), max(y1, y2) + 1), range(min(x1, x2), max(x1, x2) + 1)):
            inp_matrix[i][j] += 1
    elif check_slope == -1:
        for i, j in zip(range(min(y1, y2), max(y1, y2) + 1), range(max(x1, x2), min(x1, x2)-1, -1)):
            inp_matrix[i][j] += 1
    else:
        pass


 # added some commas and array creation code





