import os, sys
import numpy as np
from collections import defaultdict

ROOT_DIR = "/Users/curtisbalusek/Library/CloudStorage/OneDrive-Slalom/Training/aoc/2024"

def get_index(inStr: str, character='X') -> list:
    char_list, x_ind = [char for char in inStr], []
    for ind in range(len(char_list)):
        if char_list[ind]==character:
            x_ind.append(ind)
    return char_list, x_ind


def sub_matrix(inp_matrix: np.array, char_ind: tuple) -> np.array:
    ## an x has position i,j in the array
    ## if it is too close to the boundary, we don't check certain direcitons
    ## check x_position to column (0,shape(matrix))
    ## check y_position to row (0, shape(matrix))
    low_row = i-4 >= 0
    high_row = i+4 <= shape(inp_matrix)[0]-1
    left_col = j-4 >= 0
    right_col = j+4 <= shape(inp_matrix)[1]-1

    # left horizontal [i-3:i+1][j] == "SAMX"

    # right horizontal [i:i+4][j] == "XMAS"

    # vertical up [i][j-3:j+1] == "SAMX"

    # vertical down [i][j:j+4] == "XMAS"

    # Diagonal UpLeft "".join([i-3][j-3], [i-2][j-2], [i-1][j-1], [i][j]) == "SAMX"

    # diagonal upRight "".join([i][j], [i+1][j-1],[i+2][j-2], [i+3][j-3]) == "XMAS"

    # Diagonal Down Left "".join([i-3][j+3], [i-2][j+2], [i-1][j+1], [i][j]) == "SAMX"

    # Diagonal Down Right "".join([i][j], [i+1][j+1],[i+2][j+2], [i+3][j+3]) == "XMAS"
    
    
    
    
    
    
    
    
    

    x_max, y_max = shape(inp_matrix)




def read_array(inPath):
    array_dict= {}
    mat = []
    row = 0
    with open(os.path.join(ROOT_DIR, inPath)) as f:
        for line in f.readlines():
            print(row)
            proc_line, x_ind = get_index(line.rstrip())
            mat.append(proc_line)
            if row not in (array_dict.keys()):
                array_dict[row]={}
            for x in x_ind:
                array_dict[row][x] = True 
            row += 1
    return array_dict, mat 

if __name__ == '__main__':
    read_array('input_files/day4_input.txt')


