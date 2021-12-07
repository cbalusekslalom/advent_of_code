"""
Moving crabs
First should calculate the median of positions
Second will find the average of positions
"""

import numpy as np


def in_file_to_list(in_text: str) -> list:
    return [int(i) for line in open(in_text, "r") for i in line.rstrip().split(',')]


def sum_to_zero(inp: int):
    return int(inp*(inp+1)/2)


def check_fuel(in_list: list, num: int) -> int:
    return np.sum([sum_to_zero(abs(i - num)) for i in in_list])


def main(in_file):
    new_crabs = in_file_to_list(in_file)
    min_fuel, pos = 100000000, 0
    for i in range(max([i for i in new_crabs])):
        fuel_cost = check_fuel(new_crabs, i)
        if fuel_cost < min_fuel:
            min_fuel = fuel_cost
            pos = i
        else:
            continue
    print(f" The minimum fuel needed to position crabs is {min_fuel}, at {pos}")


if __name__ == '__main__':
    main('../../../../PycharmProjects/pythonProject/aoc_2021_day7_input.txt')