# sample in: be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |
# fdgacbe cefdb cefbgd gcbe
# 8 (2,3,5) (0,6,9), 4
# {t: , tl: , tr: , m: , bl: , br: , b: }
# h: d, c, f
# v: b, e, a, g
# ['be', 'edb', 'cgeb', 'fabcd', 'fdcge', 'fecdb', 'agebfd', 'cbdgef', 'fgaecd', 'cfbegad']
# [1, 7, 4, (.,.,3), (.,.,6), 8]
#in_put = 'be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb'
#input_list = in_put.split(' ')

#know 1 -> know 3 -> know horizontal & vertical

def file_reader(input_file):
    input_lists = []
    with open(input_file, 'r') as f:
        for line in f.readlines():
            input_lists.append(line.rstrip().split(' | '))
    return input_lists

def get_truth(instr, chkstr):
    status = True
    for i in chkstr:
        status = (i in instr) and status
    return status

def string_sub(inp: str, rem: str) -> str:
    inp_as_list = [char for char in inp]
    for letter in [char for char in rem]:
        # print(letter)
        if letter in inp_as_list:
            inp_as_list.remove(letter)
        else:
            pass
    return "".join(inp_as_list)

def make_mapper(input_list):
    len_5, len_6, new_dict = [], [], {}
    input_list.sort(key=len)
    for j in range(10):
        new_dict[j] = ''
    for i in input_list:
        i = "".join(sorted(i))
        if len(i) == 2:
            new_dict[1] = i
        elif len(i) == 3:
            new_dict[7] = i
        elif len(i) == 4:
            new_dict[4] = i
        elif len(i) == 7:
            new_dict[8] = i
        elif len(i) == 5:
            if get_truth(i, new_dict[1]):
                new_dict[3] = i
            else:
                len_5.append(i)
        elif len(i) == 6:
            if get_truth(i, new_dict[1]) is False:
                new_dict[6] = i
            else:
                len_6.append(i)
        else:
            pass
    for k in len_5:
        check_inp = string_sub(new_dict[4],new_dict[1])
        if get_truth(k, check_inp):
            new_dict[5] = k
        else:
            new_dict[2] = k
    for m in len_6:
        check_inp = string_sub(new_dict[3], new_dict[1])
        if get_truth(m, check_inp):
            new_dict[9] = m
        else:
            new_dict[0] = m
    return new_dict

def main():
    file_inp = file_reader('../../../../PycharmProjects/pythonProject/aoc_2021_day8_input.txt')
    sum, count = 0, 1
    for inp in file_inp:
        inp_list = inp[0].split(' ')
        inp_list.sort()
        new_dict = make_mapper(inp_list)
        rev_dict = {value: str(key) for (key, value) in new_dict.items()}
        out_list = ["".join(sorted(i)) for i in inp[1].split(' ')]
        out_list = [rev_dict[i] for i in out_list]
        sum += int("".join(out_list))
        # print(count)
        count += 1
    return sum
    """
    counter = 0
    for inp in file_inp:
        for val in inp[1].split(' '):
            if len(val) in [2, 3, 4, 7]:
                counter += 1
            else:
                pass
    print(counter)
    """

