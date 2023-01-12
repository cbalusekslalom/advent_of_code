### Breadth First search
### apply additional rules locally such that a node can only increase by max +1 from alpha_dict (doesn't say if you can drop precipitously)
import numpy as np
from collections import deque


## class of array position
class Node:

    def __init__(self, x, y, height, parent=None):
        self.x = x
        self.y = y
        self.height = height
        self.parent = parent

    def __repr__(self):
        return str((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def set_parent(self,source):
        self.parent = source


def generate_input(inFile):
    ### Read input, return Matrix, starting Node, and destination Node
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alpha_dict = {key: ind for ind, key in enumerate([i for i in alpha])}
    newArray = []
    row_counter = 0
    with open('input.txt') as f:
        for line in f.readlines():
            row = list(alpha_dict[x] if x not in ['S', 'E'] else x for x in line.rstrip())
            newArray.append(row)
            if 'S' in row:
                start_pos = (row_counter, row.index('S'))
            if 'E' in row:
                end_pos = (row_counter, row.index('E'))
            row_counter += 1
    print(start_pos, end_pos)
    return np.array(newArray), Node(start_pos[0], start_pos[1], 0), Node(end_pos[0], end_pos[1], 26)



## Possible moves
row = [-1, 0, 0, 1]
col = [0, -1, 1, 0]

def get_queue(matrix, input_pos):
    for tuple in [i for i in list(zip(row, col))]:
        if isValid(matrix.shape(), input_pos):
            return True


# should check if position is valid
def isValid(N, input_pos):
    return 0 <= input_pos[0] < N and 0 <= input_pos[1] < N

def getPath():
    return True

def findPath(matrix: np.array, start_node: Node, end_node: Node):

    N = matrix.shape()

    root = start_node.__repr__

    visited, queue = set(), deque(root)
    visited.add(root)

    while queue:
        ### Add valid neighbors to queue
        ### check if valid neighbors were visited

        def baseFirstPassMethod(sensor, beacon):
            visited_list = []
            queue = deque([beacon, sensor])

            row = [1, 0, 0, -1]
            col = [0, 1, -1, 0]

            while queue:
                pos = queue.pop()
                visited_list.append(pos)

                for tup in list(zip(row, col)):
                    if (pos[0] + tup[0], pos[1] + tup[1]) not in visited_list:
                        queue.append((pos[0] + tup[0], pos[1] + tup[1]))

                if beacon in visited_list:
                    break

            return visited_list