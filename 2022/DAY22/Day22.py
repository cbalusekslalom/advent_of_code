
with open('input.txt') as f:
    array_dict = {}
    counter = 1
    for line in f.readlines():
        if line == '\n':
            break
        if counter not in array_dict.keys():
            array_dict[counter] = []
        array_dict[counter] = [i for i in line.replace('\n','').replace(' ','X')]
        counter += 1

with open('instructions.txt') as i:
    instructions = i.readline()

print(array_dict)
print(instructions)

"""
Row is the dict_key
idx is the column #
need a heading
"""

class Walker:
    def __init__(self, map_dict, instructions):
        self.map = map_dict
        self.instructions = instructions
        self.start_row = 1
        self.start_col = min([idx for idx in self.map if idx == '.'])
        self.heading = 0

    def change_heading(self, inp):
        if inp == 'R':
            self.heading = (self.heading + 1) % 4
        elif inp == 'L':
            self.heading = (self.heading - 1) % 4
        else:
            print('invalid direction')

    def

