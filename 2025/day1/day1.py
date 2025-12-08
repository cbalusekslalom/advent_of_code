import os, sys 
import numpy as np

class Safe():
    """
    A new AoC safe object for checking the password
    """
    def __init__(self):
        self.location = 50
        self.zeros = 0
        self.pass_zero = 0

    def movement(self, inp:str):
        if not inp:
            raise ValueError()
        if inp[0] == 'R':
            temp = self.location+int(inp[1:])
        elif inp[0] == 'L':
            temp = self.location-int(inp[1:])
        self.location = np.mod(temp, 100)
        if not self.location:
            print(f"the dial will rotate: {temp}, on {inp}; this will count for 1")
            self.zeros += 1
            self.pass_zero += 1
        if temp >= 100 or temp <= 0:
            print(f"the dial will rotate: {temp} in {inp}; this will count for 1 + {int(temp/100)}")
            self.pass_zero += 1
            self.pass_zero += int(temp/100)
    
    def get_zeros(self):
        return self.zeros
    def get_zero_passes(self):
        return self.pass_zero

def main():
    newSafe = Safe()
    print("A new Safe has been found")
    with open(os.path.join(os.getcwd(), '2025/inputs/day1.txt'), 'r') as f:
        for line in f.readlines():
            newSafe.movement(line)
    print(newSafe.get_zeros())
    print(newSafe.get_zero_passes())

main()