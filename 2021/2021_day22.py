"""
3D matrix update
input line: 'on x=-5..46,y=-32..20,z=-18..26\n'
"""
import numpy as np


def create_n_dim_3d_matrix(n):
    return np.zeros((n, n, n), dtype=int)


def read_in_file(in_file):
    on_off_list = []
    with open(in_file,'r') as f:
        for line in f.readlines():
            line = line.rstrip()
            state_coord = line.split(' ')
            state, coordlist = state_coord[0], state_coord[1].split(',')
            coord_dict = {}
            for i in coordlist:
                new_key = i.split('=')[0]
                values = i.split('=')[1].split('..')
                value_list = [int(val) for val in values]
                coord_dict[new_key] = value_list
            on_off_list.append([state, coord_dict])
    return on_off_list


class Cube:
    def __init__(self, state, xrange, yrange, zrange):
        self.state = [1 if state == 'on' else 0][0]
        self.vertices = {}
        self.xrange = xrange
        self.yrange = yrange
        self.zrange = zrange

    def plot_vertices(self):
        counter = 1
        for x in self.xrange:
            for y in self.yrange:
                for z in self.zrange:
                    self.vertices[counter] = [x, y, z]
                    counter += 1

new_matrix = create_n_dim_3d_matrix(101)
new_input = read_in_file('2021_day22_input.txt')
for i in new_input:
    pad = 50
    state = i[0]
    input_dictionary = i[1]
    xmin, xmax = input_dictionary['x'][0] + pad, input_dictionary['x'][1] + 1 + pad
    ymin, ymax = input_dictionary['y'][0] + pad, input_dictionary['y'][1] + 1 + pad
    zmin, zmax = input_dictionary['z'][0] + pad, input_dictionary['z'][1] + 1 + pad
    if xmin < 0 or xmax > 100 or ymin < 0 or ymax > 100 or zmin < 0 or zmax > 100:
        pass
    else:
        for x in range(xmin, xmax):
            for y in range(ymin, ymax):
                for z in range(zmin, zmax):
                    if state == 'on':
                        new_matrix[x, y, z] = 1
                    else:
                        new_matrix[x, y, z] = 0

