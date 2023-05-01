### Create sensor class
### Create sensor matrix of distances
import numpy as np
import sys
numpy.set_printoptions(threshold=sys.maxsize)

def read_input(in_file):
    new_obj_list = []
    with open(in_file, 'r') as f:
        for line in f:
            if line.startswith('---'):
                new_name = line.rstrip()
                new_coord_list = []
            elif line.startswith('\n'):
                new_obj_list.append([new_name, new_coord_list])
            else:
                coord = [int(i) for i in line.rstrip().split(',')]
                new_coord_list.append(coord)
    return new_obj_list




def measure_distance(input1, input2):
    x_dist = input2[0] - input1[0]
    y_dist = input2[1] - input1[1]
    if len(input1) == 3 and len(input2) == 3:
        z_dist = input2[2] - input1[2]
    else:
        z_dist = 0
    return np.sqrt(x_dist**2 + y_dist**2 + z_dist**2)


class Sensor:

    def __init__(self, name, beacon_list):
        self.name = name
        self.location = [0, 0, 0]
        self.beacons = beacon_list
        self.beacon_overlap_list = self.build_beacon_overlap()

    def build_beacon_overlap(self):
        beacon_temp = self.beacons
        beacon_overlap_list = []
        while len(beacon_temp) > 0:
            beacon = beacon_temp.pop(0)
            for j in beacon_temp:
                beacon_overlap_list.append(measure_distance(beacon, j))
        beacon_overlap_list.sort()
        return beacon_overlap_list

    def build_beacon_matrix(self):
        for i, k in enumerate(self.beacons):
            for j, m in enumerate(self.beacons):
                self.output_matrix[i][j] = measure_distance(k, m)


def build_beacon_overlap(list_of_beacons):
    beacon_temp = list_of_beacons
    beacon_overlap_list = []
    while len(beacon_temp) > 0:
        beacon = beacon_temp.pop(0)
        for j in beacon_temp:
            beacon_overlap_list.append(measure_distance(beacon, j))
    return beacon_overlap_list


def build_matrix(input_list):
    output_matrix = np.zeros((len(input_list),len(input_list)), dtype=float)
    for i, k in enumerate(input_list):
        for j, m in enumerate(input_list):
            output_matrix[i][j] = measure_distance(k, m)
    return output_matrix


def list_compare(list1, list2):
    return len([x for x in list1 if x in list2])

###
"""
--- scanner 0 ---
[[0,0], [0,2], [4,1], [3,3]]

--- scanner 1 ---
[[0, 0], [-1,-1], [-5,0], [-2,1]]
"""