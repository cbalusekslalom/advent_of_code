"""
step 1: set w, y, z to input
step 2: set w to input, y and z to 12+w
step 3: set w to input, y and z to 14+w
step 4: same as step 1 (possible multiplier effect)
"""
import numpy as np

class MONAD:
    def __init__(self, instruction_list):
        self.instruction_list = instruction_list
        self.x = 0
        self.y = 0
        self.z = 0
        self.w = 0
        self.attributes = {"w": self.w, "x": self.x, "y": self.y, "z": self.z}

    def inp(self, var, val):
        self.attributes[var] = val

    def add(self, inp1, inp2):
        self.attributes[inp1] += [self.attributes[inp2] if inp2 in ['x', 'y', 'z', 'w'] else inp2][0]

    def mul(self, inp1, inp2):
        self.attributes[inp1] *= [self.attributes[inp2] if inp2 in ['x', 'y', 'z', 'w'] else inp2][0]

    def div(self, inp1, inp2):
        holding_value = [self.attributes[inp2] if inp2 in ['x', 'y', 'z', 'w'] else inp2][0]
        if holding_value != 0:
            self.attributes[inp1] = int(np.floor(self.attributes[inp1]/holding_value))
        else:
            ValueError

    def mod(self, inp1, inp2):
        holding_value = [self.attributes[inp2] if inp2 in ['x', 'y', 'z', 'w'] else inp2][0]
        if holding_value != 0:
            self.attributes[inp1] = self.attributes[inp1] % holding_value
        else:
            ValueError

    def eql(self, inp1, inp2):
        if self.attributes[inp1] == [self.attributes[inp2] if inp2 in ['x', 'y', 'z', 'w'] else inp2][0]:
            self.attributes[inp1] = 1
        else:
            self.attributes[inp1] = 0

    def reset(self, input_dict=None):
        if input_dict:
            for key in self.attributes.keys():
                self.attributes[key] = input_dict[key]
        else:
            for key in self.attributes.keys():
                self.attributes[key] = 0

    def run_list(self, inp_val):
        for i in self.instruction_list:
            commands = i.split(' ')
            func = getattr(self, commands[0])
            if commands[0] == 'inp':
                func(commands[1], inp_val)
            elif commands[0] == 'eql':
                func(commands[1], (commands[2] if commands[2] in ['x', 'y', 'z', 'w'] else int(commands[2])))
            else:
                func(commands[1], (commands[2] if commands[2] in ['x', 'y', 'z', 'w'] else int(commands[2])))
        print(self.attributes)


def read_in_file(in_file):
    out_dict = {i:'' for i in range(1,15)}
    new_input = []
    j = 1
    with open(in_file, 'r') as file:
        for line in file.readlines():
            if line.startswith('inp'):
                if len(new_input) > 0:
                    out_dict[j] = MONAD(new_input)
                    j += 1
                    new_input = []
                new_input.append(line.rstrip())
            else:
                new_input.append(line.rstrip())
        out_dict[j] = MONAD(new_input)
    return out_dict


for key in new_list_of_monad.keys():


"""
start with 1st input sequence with 9
go to next input sequence with output as input
iterate to last input sequence
check output.z == 0
if not, go up to 13th and iterate to next



for i in range(9, 0, -1):
    update_monad_object with i
if ind == 14 
    if monad.z == 0:
        
else:
     
"""
def find_greatest_number(input_dict, int_key, inp_int):
    monad_obj = input_dict[int_key]
    monad_obj.reset(input_dict[int_key-1])
    monad_obj.run_list(inp_int)
    if int_key == 14:
        if monad_obj.z == 0:

    else:
        for int_val in range(9,0,-1):
            find_greatest_number(input_dict, int_key+1, int_val)

