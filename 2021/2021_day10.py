import numnpy as np

dict_match = {'{':'}', '[':']', '(':')', '<':'>'}
inv_match = {'}':'{', ']':'[', ')':'(', '>':'<'}
error_dict = {')': 3, ']': 57, '}': 1197, '>': 25137}
compl_dict = {')': 1, ']': 2, '}': 3, '>': 4}


def read_file(inp_file):
    invalid_strings = []
    corrupt_checksum = 0
    with open(inp_file, 'r') as f:
        for line in f.readlines():
            in_line = valid_check(line.rstrip(), 'c')
            if in_line[0] == 'incomplete':
                invalid_strings.append(line.rstrip())
            elif in_line[0] == 'corrupt':
                corrupt_checksum += in_line[1]
    print(corrupt_checksum)
    return invalid_strings



def point_val(inp: str, check_dict: dict) -> int:
    if inp in check_dict.keys():
        return check_dict[inp]
    else:
        return 0


def check_sum(inp_list):
    check_sum = 0
    for inp in inp_list:
        status, value = valid_check(inp)
        if status == 'corrupt':
            check_sum += value
    return check_sum



def valid_check(inp_str: str, check_type='i'):
    if check_type == 'i':
        chk_dict = {')': 1, ']': 2, '}': 3, '>': 4}
    elif check_type == 'c':
        chk_dict = {')': 3, ']': 57, '}': 1197, '>': 25137}
    else:
        chk_dict = {}
    new_stack = []
    inp_list = [char for char in inp_str[::-1]]
    run_while, status = True, ''
    while run_while:
        if len(inp_list) == 0:
            if len(new_stack) == 0:
                status = 'complete'
            else:
                status = f'incomplete'
            print(f'list finished')
            run_while = False
        else:
            check_val = inp_list.pop()
            if check_val in ['{','[','<','(']:
                new_stack.append(check_val)
            elif check_val in ['}',']','>',')']:
                if len(new_stack) == 0:
                    print(f'corrupted termination sequence at {check_val}')
                    run_while, status = False, f'corrupt'
                else:
                    pri_val = new_stack.pop()
                    if check_val == dict_match[pri_val]:
                        continue
                    else:
                        print(f'corrupted termination sequence at {check_val}')
                        run_while, status = False, f'corrupt'
            else:
                print('invalid input')
                status = 'corrupt'
                run_while = False
    if check_type == 'c':
        print(f'Final status: {status} with {point_val(check_val, chk_dict)} points')
        return status, point_val(check_val, chk_dict)
    elif check_type == 'i':
        print(new_stack)
        inc_checksum = 0
        while len(new_stack) > 0:
            inc_checksum *= 5
            val = new_stack.pop()
            opp_val = dict_match[val]
            inc_checksum += chk_dict[opp_val]
        print(f'the total points for this list is {inc_checksum}')
        return status, inc_checksum


sum_list = []
for i in new_invalid:
    sum_list.append(valid_check(i, 'i')[1])