## 0 -> current bank
## 1 -> inc/dec
## 2 -> amount (+/-)
## 3 -> if
## 4 -> ref bank
## 5 -> condition
## 6 -> value

register = {}
max_inp = 0

def equivalence_fn(inValue: int, eq: str, value: int) -> bool:
    eq_dic = {
        '>': inValue > value,
        '<': inValue < value,
        '!=': inValue != value,
        '==': inValue == value,
        '<=': inValue <= value,
        '>=': inValue >= value
    }
    return eq_dic[eq]


with open('input.txt') as f:
    for line in f.readlines():
        line_input = line.split()
        if line_input[0] not in register.keys():
            register[line_input[0]] = 0
        if line_input[4] not in register.keys():
            register[line_input[4]] = 0
        if line_input[1] == 'inc':
            controller = 1
        else:
            controller = -1
        change = controller * int(line_input[2])
        if equivalence_fn(register[line_input[4]], line_input[5], int(line_input[6])):
            register[line_input[0]] += change

        if register[line_input[0]] > max_inp:
            max_inp = register[line_input[0]]
print(max(register.values()))
print(max_inp)