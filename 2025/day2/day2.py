import os, sys 
from collections import defaultdict
import numpy as np

## a string is 123123 -> str[0:3] == str[3:]
## 1234123 doesn't qualify
## 12341234 str[0:4] == str[4:]

def split_list_by_chunk_size(lst, n):
    result = []
    for i in range(0, len(lst), n):
        result.append(lst[i:i + n])
    return result

def check_drome(i) -> bool:
    if not type(i) is str:
        i = str(i) 
    if len(i)%2 == 1:
        return 0 
    middle_pt = int(len(i)/2)
    if i[0:middle_pt] == i[middle_pt:]:
        return int(i)
    return 0

def check_drome_ii(i) -> bool:
    if not type(i) is str:
        i = str(i) 
    for j_len in range (1, int(np.floor(len(i)/2))+1):
        if len(i)%j_len == 0:
            if len(set(split_list_by_chunk_size(i, j_len))) == 1:
                return int(i)
    return 0

    ## if len(i)%j_len == 0
    ## 1 if i, i+1, ..., n are equal then true
    ## 2 if [i, i+1], [i+2,i+3], ... [n-1, n] are equal then true
    ## 3 if [i:i+3] == [i+3:i+6] == [i+6:i+9] ... [n-2:] are equal then true
    middle_pt = int(len(i)/2)
    if i[0:middle_pt] == i[middle_pt:]:
        return int(i)
    return 0

def read_file(inTxt:str):
    with open(os.path.join(os.getcwd(),'2025/inputs/'+inTxt),'r') as f:
        inLineList = f.readline().split(',')
    return inLineList

def run_main(inTxt):
    inList = read_file(inTxt)
    tot_sum = 0
    for pair in inList:
        print(pair)
        elements = [i for i in range(int(pair.split('-')[0]), int(pair.split('-')[1]))]
        tot_sum += sum(map(check_drome, elements))
    print(tot_sum)
    return tot_sum

def run_main_ii(inTxt):
    inList = read_file(inTxt)
    tot_sum = 0
    for pair in inList:
        print(pair)
        elements = [i for i in range(int(pair.split('-')[0]), int(pair.split('-')[1]))]
        tot_sum += sum(map(check_drome_ii, elements))
    print(tot_sum)
    return tot_sum

if __name__ == '__main__':
    run_main_ii('day2.txt')
