def read(inFile):
    instructs = []
    with open(inFile) as f:
        for line in f.readlines():
            instructs.append(line)
    return instructs

class Register:

    def __init__(self, n):
        self.register = n
        self.cycle = 1
        self.cycle_dict = {self.cycle:self.register}

    def noop_advance(self):
        self.cycle += 1
        self.cycle_dict_append()

    def advx(self, inp):
        self.cycle += 1
        self.cycle_dict_append()
        self.cycle += 1
        self.cycle_dict_append()
        self.register += inp
        self.cycle_dict_append()

    def cycle_dict_append(self):
        self.cycle_dict[self.cycle] = self.register


def main():
    new_register = Register(1)
    instructions = read('input.txt')
    #instructions = ['noop', 'addx 3', 'addx -5']
    for inp in instructions:
        if inp.rstrip() == 'noop':
            new_register.noop_advance()
        elif inp.split()[0] == 'addx':
            new_register.advx(int(inp.split()[1]))
        else:
            print("invalid instructions")
        print(inp, new_register.cycle%40, new_register.register)
    new_register.noop_advance()
    new_register.noop_advance()
    print([(key, new_register.cycle_dict[key]) for key in new_register.cycle_dict.keys() if key in [20, 60, 100, 140, 180, 220]])
    print(sum([key*new_register.cycle_dict[key] for key in new_register.cycle_dict.keys() if key in [20, 60, 100, 140, 180, 220]]))

    crt = {}
    for i in range(241):
        cycle = i+1
        if i % 40 in [new_register.cycle_dict[cycle]-1, new_register.cycle_dict[cycle], new_register.cycle_dict[cycle]+1]:
            crt[i] = '#'
        else:
            crt[i] = '.'

    for i in range(int(260/40)+1):
        print(''.join([value for value in crt.values()])[40*i:40*(i+1)])


"""
    20*22
    60*21 (24)
    100*21 (17)
    140*19 (17)
    180*21 (24)
    220*16 (22)
"""

if __name__ == "__main__":
    main()
