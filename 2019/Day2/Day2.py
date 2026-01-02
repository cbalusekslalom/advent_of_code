import os, sys
from typing import Self

current_path = os.path.dirname(__file__)
input_path = os.path.relpath("../Inputs/Day2.txt", current_path)

class Intcode:
    def __init__(self, inList, index=0):
        inDict = {}
        for i in range(len(inList)):
            inDict[i] = inList[i]
        self.inputDict = inDict
        self.index = index
    
    def get_intcode(self):
        return self.inputDict

    def update_pos(self, pos1, inputVal):
        self.inputDict[pos1] = inputVal

    def get_pos(self, pos1):
        return self.inputDict[pos1]
    
    def run_intcode(self):
        while self.inputDict[self.index] != 99:
            pos1 = self.inputDict[self.index+1]
            pos2 = self.inputDict[self.index+2]
            pos3 = self.inputDict[self.index+3]
            if self.inputDict[self.index] == 1:
                self.inputDict[pos3] = self.inputDict[pos1] + self.inputDict[pos2]
            elif self.inputDict[self.index] == 2:
                self.inputDict[pos3] = self.inputDict[pos1] * self.inputDict[pos2]                
            else: 
                print("unsupported operation")
            self.index += 4
        print(self.get_pos(0))  
    
def get_input(inputFile):  
    with open(inputFile, "r") as inFile:
        inList = list(map(int, inFile.readline().split(',')))
    return inList 

def get_special_number(inList, inp: int) -> int:
    for i in range(100):
        for j in range(100):
            new_code = Intcode(inList)
            new_code.update_pos(1,i)
            new_code.update_pos(2,j)

        if new_code.get_pos(0) == inp:
            print(f"The combo is {100*i+j}.")


def main():
    new_intcode = Intcode(get_input(input_path))
    new_intcode.update_pos(1, 12)
    new_intcode.update_pos(2,2)
    
    new_intcode.run_intcode()

    ### get_special_number(get_input(input_path), 19690720)

if __name__ == "__main__":
    main(input_path)
