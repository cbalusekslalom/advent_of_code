import sys, os
import numpy as np

"""
Code was working, went to rebase into a dictionary instead of in list.  haven't completed. 
Correct input achieved prior
"""



inPath = os.getcwd()  ## 'Users/curtis.balusek/Documents/Training/aoc'
filename = '2018/Day1/2018_day1_input.txt'  ##
inFile = os.path.join(inPath, filename)


def dup_check(val: int, inputDict: dict):
    if len(inputDict) == 0:
        return "Must push an inputDict"
    if val not in inputDict.keys():
        inputDict[val] = 1
        return False, inputDict
    else:
        inputDict[val] += 1
        return True, inputDict

def get_freq_adjustment(position,adjustment):
    operation = adjustment[0]
    distance = int(adjustment[1:])
    if operation == '+':
        position += distance
    elif operation == '-':
        position -= distance
    else:
        return "Issue with operation"
    return position

def main(inFile):
    adjustment_list = []
    with open(inFile) as f:
        for line in f.readlines():
            adjustment_list.append(line)

    starting_pos = 0
    duplicate_found = False
    dup_dict = {0: True}
    iter_count = 0
    while not duplicate_found:
        iter_count += 1
        print(f"working on file iteration {iter_count}")

                duplicate_found = dup_check(starting_pos, dup_list)
                if duplicate_found:
                    return starting_pos
                else:
                    dup_list.append(starting_pos)
    return starting_pos


if __name__ == '__main__':
    main(inFile)
