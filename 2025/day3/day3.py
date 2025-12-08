import os, sys

#processing, readline, process, get number proceed

def get_all_pairs_nested_loops(input_list):
    pairs = []
    n = len(input_list)
    for i in range(n):
        for j in range(i + 1, n):
            pairs.append(input_list[i]*10 + input_list[j])
    return max(pairs)

def get_all_pairs_nested_loops_ii(input_list):
    number = 0
    n = len(input_list)
    counter = 11
    temp_list = input_list
    while counter > -1:
        digit = max(temp_list[0:n-counter])
        digit_position = temp_list.index(digit)
        number += digit*10**(counter) 
        temp_list = temp_list[digit_position+1:]
        n = len(temp_list)
        counter -= 1
    print(number)
    return number


def joltage(inString: str) -> int:
    input_list = [int(intgr) for intgr in inString]
    outvalue = get_all_pairs_nested_loops(input_list)
    outvalue2 = get_all_pairs_nested_loops_ii(input_list)
    print(outvalue)
    print(outvalue2)
    return outvalue2


def read_file(inTxt:str):
    total_sum = 0
    with open(os.path.join(os.getcwd(), '2025/inputs/'+inTxt), 'r') as f:
        for line in f.readlines():
            ## process a line
            line = line.strip()
            total_sum += joltage(line)
    print(total_sum)
    return total_sum

if __name__ == '__main__':
    read_file('day3.txt')