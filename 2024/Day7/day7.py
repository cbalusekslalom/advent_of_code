import sys

sys.path.append('/Users/curtisbalusek/Library/CloudStorage/OneDrive-Slalom/Training/aoc/2024/input_files')


sample = """
194558: 2 6 664 40 874 40 7
127536599: 49 4 21 65 99 -> +,+,+,+ -> +,+,+,* -> 
[99*65, 99+65]
"""

def read_infile(inPath:str):
    out_value = 0
    with open(inPath) as f:
        for line in f.readlines():
            line_split = line.split(': ')
            total = int(line_split[0])
            line_list = [int(i) for i in line_split[1].split(' ')]
            print(line)
            recursive_process(total, line_list)
            if recursive_process(total, line_list):
                out_value += total
    print(f'the total output is: {out_value}')
    return out_value
## I think a tree traversal is more correct, but I don't want to code it rn

def recursive_process(total:int, inList: list):
    proc_list = [inList[0]]
    temp_list = []
    for i in range(1,len(inList)):
        list_element = inList[i]
        while proc_list != []:
            val = proc_list.pop()
            mult, plus, concat = list_element*val, list_element+val, int(str(val) + str(list_element))
            print(total, mult, plus, concat)
            temp_list.append(mult)
            temp_list.append(plus)
            temp_list.append(concat)

        proc_list.extend(temp_list)
        temp_list = []
    return total in proc_list

if __name__ =="__main__":
    read_infile('input_files/day7_input.txt')