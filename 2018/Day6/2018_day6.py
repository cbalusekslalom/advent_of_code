"""
Metropolis Criterion
"""

def read_file(in_text: str):
    max_x, max_y = 0, 0
    coord_list = []
    with open(in_text, 'r') as f:
        for line in f.readlines():
            coord = [int(i) for i in line.split(', ')]
            if coord[0] > max_x:
                max_x = coord[0]
            if coord[1] > max_y:
                max_y = coord[1]
            coord_list.append(coord)
    print(f"Need an array of n-size {max(max_x, max_y)}")
    return coord_list


def make_matrix(n: int):
    return [[0] * n for ind in range(n)]

