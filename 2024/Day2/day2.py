import os, sys

ROOT_PATH = '/Users/curtisbalusek/Library/CloudStorage/OneDrive-Slalom/Training/aoc/2024'

def gt(int1, int2):
    return (True if int1 > int2 and int1 - int2 <= 3 else False)

def lt(int1, int2):
    return (True if int1 < int2 and int2 - int1 <= 3 else False)

def check_list(inList:list, i, ad) -> bool:
    if i == len(inList):
        return True
    while i+1 < len(inList):
        if ad:
            if inList[i] < inList[i+1] and inList[i+1]-inList[i] <=3:
                pass
            else:
                return False
        else:
            if inList[i] > inList[i+1] and inList[i]-inList[i+1] <=3:
                pass
            else:
                return False
        return check_list(inList, i+1, ad)
        
def check_single(inList, i, ad):
    popped = 0
    if i == len(inList):
        return True
    while i+1 < len(inList):
        if ad:
            if inList[i] < inList[i+1] and inList[i+1]-inList[i] <=3:
                pass
            else:
                inList.pop(i+1)
        else:
            if inList[i] > inList[i+1] and inList[i]-inList[i+1] <=3:
                pass
            else:
                return False
        return check_list(inList, i+1, ad)


def process_line(inStr:str) -> bool:
    inList = [int(i) for i in inStr.strip().split(' ')]
    ad = (inList[0] <= inList[1]) ## ad true is asc false is desc
    return check_list(inList, 0, ad, gap)

def read_file(path_for_file):
    total_safe = 0
    with open(os.path.join(ROOT_PATH,path_for_file)) as f:
        for line in f.readlines():
            if process_line(line) is None:
                print(line)
                total_safe += 1
    print(f'the total safe rows are {total_safe}')

if __name__=='__main__':
    read_file('input_files/day2_input.txt')