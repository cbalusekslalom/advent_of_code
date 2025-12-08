import os, sys 

def check_fresh(inVal, inList) -> bool:
    for tpl in inList:
        if inVal in range(int(tpl[0]),int(tpl[1]+1)):
            return True
    return False

def read_file(inTxt:str):
    tpl_list = []
    inp_list = []
    with open(os.path.join(os.getcwd(),'2025/inputs/' +inTxt), 'r') as f:
        for line in f.readlines():
            if line == '\n':
                continue
            if '-' in line:
                sub_list = [int(i) for i in line.strip().split('-')]
                tpl_list.append(sub_list)
            else:
                inp_list.append(int(line.strip()))
    return tpl_list, inp_list
            
def main(input_file_name):
    tpl_list, inp_list = read_file(input_file_name)
    bool_results = [check_fresh(i, tpl_list) for i in inp_list]
    print(sum(bool_results))
    print("next step")
    print(check_fresh_list(tpl_list))

    return bool_results

def check_two_tuples(inTpl1: tuple, inTpl2: tuple):
    tpl1_lower, tpl1_upper = inTpl1[0], inTpl1[1]
    tpl2_lower, tpl2_upper = inTpl2[0], inTpl2[1]
    if tpl2_upper < tpl1_lower or tpl1_upper < tpl2_lower:
        return False 
    elif tpl1_lower < tpl2_lower and tpl2_upper < tpl1_upper:
        return [tpl1_lower, tpl1_upper]
    elif tpl2_lower < tpl1_lower and tpl1_upper < tpl2_upper:
        return [tpl2_lower, tpl2_upper]
    elif tpl1_lower < tpl2_lower and tpl1_upper < tpl2_upper:
        return [tpl1_lower, tpl2_upper]
    elif tpl2_lower < tpl1_lower and tpl2_upper < tpl1_upper:
        return [tpl2_lower, tpl1_upper]
    else:
        return False


def check_fresh_list(inp_list) -> int:
    ## take a range of values
    ## if those range of values not in my list of ranges, add it to the list of ranges
    ## take another list of ranges
    ## this can either not be in the list of ranges OR in the list of ranges
    min_max_list = []
    temporary_mm = []
    temp_list = inp_list
    while len(temp_list) > 0:
        print(min_max_list)
        inp = temp_list.pop()
        inp_lower, inp_upper = int(inp[0]), int(inp[1])
        if len(min_max_list) == 0:
            min_max_list.append(inp)
            continue
        for item in min_max_list:
            check_tpls = check_two_tuples(inp, item)
            if not check_tpls:
                temporary_mm.append(inp)
            else:
                temporary_mm.append(check_tpls)
        min_max_list = temporary_mm
            
    return min_max_list


if __name__=='__main__':
    main('day5_test.txt')

