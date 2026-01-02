import os
import math

current_path = os.path.dirname(__file__)
input_path = os.path.relpath('../Inputs/Day1.txt', current_path)
print(input_path)

def proc_mass(input: int) -> int:
    return math.floor(input/3)-2

def main(input_path):
    with open(input_path,"r") as inputFile:
        total_mass = 0
        for line in inputFile.readlines():
            sub_total_mass = 0
            new_mass = proc_mass(int(line.strip()))
            while new_mass > 0:
                sub_total_mass += new_mass
                new_mass = proc_mass(new_mass)
            total_mass += sub_total_mass
    print(f"""The total mass is {total_mass}""")

if __name__ == "__main__":
    main(input_path)
