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
        inp = inp.strip()
        if not inp:
            raise ValueError()
        val = int(inp[1:])
        if val > 99:
            counter = int(val/100)
            inp2 = val%100
        if inp[0] == 'R':
            temp = self.location+int(inp[1:])
        elif inp[0] == 'L':
            temp = self.location-int(inp[1:])
        print(f"The input is {inp}, this will move from {self.location} to {temp}")
        if temp >= 100:
            self.pass_zero += 1 + int(abs((temp)/100)-1)
        if temp < 0:
            self.pass_zero += 1 + int(abs((temp)/100)-1) 
        self.location = np.mod(temp, 100)
        if not self.location:
            print(f"the dial will rotate: {temp}, on {inp}; this will count for 1")
            self.zeros += 1
    def get_zeros(self):
        return self.zeros
    def get_zero_passes(self):
        return self.pass_zero

def main(inTxt):
    newSafe = Safe()
    print("A new Safe has been found")
    with open(os.path.join(os.getcwd(), '2025/inputs/'+inTxt), 'r') as f:
        for line in f.readlines():
            newSafe.movement(line)
    print(newSafe.get_zeros())
    print(newSafe.get_zero_passes())

main('day1_test.txt')