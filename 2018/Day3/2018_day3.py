""
import numpy as np
import matplotlib as plt

def read_input(in_file):
    claim_list, coord_list, sq_list = [], [], []
    with open(in_file, 'r') as f:
        for line in f:
            in_line = line.rstrip().split(' ')
            claim_list.append(in_line[0])
            coord = in_line[2].rstrip(':').split(',')
            dim = in_line[-1].split('x')
            coord_list.append(coord)
            sq_list.append(dim)
    return claim_list, coord_list, sq_list


def new_grid(n):
    return [['0'] * n for i in range(n)]


def update_grid(grid, inp_coord, dims, claim_val):
    claim_overlaps = []
    inp_x, inp_y = int(inp_coord[0]), int(inp_coord[1])
    for xval in range(inp_x, inp_x+int(dims[0])):
        for yval in range(inp_y, inp_y+int(dims[1])):
            update_cell = grid[xval][yval]
            if update_cell == '0':
                grid[xval][yval] = claim_val
            elif update_cell != '0':
                if update_cell not in claim_overlaps:
                    print(f'overlap detected between {claim_val} and {update_cell}')
                    claim_overlaps.append(update_cell)
                else:
                    pass
                grid[xval][yval] = claim_val
    return grid, claim_overlaps


def main(in_file):
    claim_list, coord_list, sq_list = read_input(in_file)
    dispute_list = claim_list
    grid = new_grid(1100)
    for coords, sqs, claims in list(zip(coord_list, sq_list, claim_list)):
        grid, disputes = update_grid(grid, coords, sqs, claims)
        print(claims, disputes)
        if len(disputes) > 0:
            dispute_list.remove(claims)
        for disp in disputes:
            if disp in dispute_list:
                dispute_list.remove(disp)
    print(dispute_list)

