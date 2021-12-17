hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
bin_list = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100',
            '1101', '1110', '1111']

version_dic = {'000':'0', '001':'1', '010':'2', '011':'3', '100':'4', '101':'5', '110':'6', '111':'7'}
hex_dic = dict(zip(hex_list, bin_list))

"""
TYPE 0: SUM
TYPE 1: PRODUCT
TYPE 2: MINIMUM
TYPE 3: MAXIMUM
TYPE 4: LITERAL
TYPE 5: BOOL if packet 1 > packet 2
TYPE 6: BOOL if packet 1 < packet 2
TYPE 7: BOOLean if packet 1 = packet 2
"""
import math


def read_in_file(in_file, dict_obj):
    with open(in_file, 'r') as f:
        default_list = [char for char in f.readline().rstrip()]
    binary_number = ''
    for i in default_list:
        binary_number += dict_obj[i]
    return binary_number


version_list = []

def type_function(type: str, input_list: list):
    if type == '0':
        return sum(input_list)
    elif type == '1':
        return math.prod(input_list)
    elif type == '2':
        return np.min(input_list)
    elif type == '3':
        return np.max(input_list)
    elif type == '5':
        if input_list[0] > input_list[1]:
            return 1
        else:
            return 0
    elif type == '6':
        if input_list[0] < input_list[1]:
            return 1
        else:
            return 0
    elif type == '7':
        if input_list[0] == input_list[1]:
            return 1
        else:
            return 0



def recursive_list_input(inp_string):
    version = inp_string[:3]
    global version_list
    version_list.append(version)

    type = inp_string[3:6]
    if type == '100':
        return_string = ''
        check_pos = 6
        while inp_string[check_pos] == '1':
            return_string += inp_string[check_pos+1:check_pos+5]
            check_pos += 5
        return_string += inp_string[check_pos + 1:check_pos + 5]
        check_pos += 5
        literal_int = int('0b'+return_string,2)
        print('v' + version_dic[version] + '.' + version_dic[type] + '.L' + str(literal_int))
        remaining_in_letter = 4-(check_pos % 4)
        return literal_int, inp_string[check_pos:]
    else:
        check_val = inp_string[6]
        if check_val == '0':
            binary_bits = inp_string[7:22]
            number_bits_in_subset = int('0b'+binary_bits,2)
            print('v' + version_dic[version] + '.' + version_dic[type] + '.B' + str(number_bits_in_subset))
            sub_string = inp_string[22:22+number_bits_in_subset]
            int_list = []
            while len(sub_string) > 0:
                ret_value, sub_string = recursive_list_input(sub_string)
                int_list.append(ret_value)
            return_value = type_function(version_dic[type], int_list)
            return return_value, inp_string[22+number_bits_in_subset:]
        else:
            binary_bits = inp_string[7:18]
            counter = int('0b'+binary_bits, 2)
            print('v' + version_dic[version] + '.' + version_dic[type] + '.C' + str(counter))
            sub_string = inp_string[18:]
            int_list = []
            while counter > 0:
                ret_value, sub_string = recursive_list_input(sub_string)
                int_list.append(ret_value)
                counter -= 1
            return_value = type_function(version_dic[type], int_list)
            return return_value, sub_string
