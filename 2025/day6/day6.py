import os, sys 
import operator
from functools import reduce

operations_dict = {
        '*': operator.mul,
        '+': operator.add
}

class Homework:
    def __init__(self, inTxt):
        self.input_file = os.path.join(os.getcwd(), '2025/inputs/'+inTxt)
        self.operations = []
        self.line_dict = {}
        self.line_dict_ii = {}
        self.read_file
        self.total_sum = 0
    @property
    def read_file(self):
        counter = 0
        with open(self.input_file, 'r') as f:
            for line in f.readlines():
                if line[0] in ('*','+'):
                    self.operations = [lin for lin in line.split(' ') if lin != '']
                else:
                    self.line_dict[counter] = [int(inp.strip()) for inp in line.split()]
                    counter += 1
    @property
    def get_operations(self):
        if not self.operations:
            return None 
        return self.operations
    def get_line(self, int):
        if not int in self.line_dict.keys():
            return None 
        return self.line_dict[int]
    @property
    def run_sum(self):
        sum = 0
        for idx, operation in enumerate(self.operations):
            sum += [reduce(operations_dict[operation], [self.line_dict[key][idx] for key in self.line_dict.keys()])]
        return sum
    @property
    def get_total_sum(self):
        return self.total_sum


"""
def main(inTxt):
    new_homework = Homework(inTxt)
    l1 = new_homework.get_first_line
    l2 = new_homework.get_second_line
    l3 = new_homework.get_third_line 
    op = new_homework.get_operations
total_sum = 0
for i in range(len(op)):
    operation = op[i]
    if operation == '+':
        total_sum += l1[i] + l2[i] + l3[i]
    if operation == '*':
        total_sum += l1[i] * l2[i] * l3[i]
    return total_sum

if __name__ == '__main__':
    tot_sum = main('day6.txt')
    print(tot_sum)
"""