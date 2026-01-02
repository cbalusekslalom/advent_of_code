import re
import sys, os

ROOT_DIR = "/Users/curtisbalusek/Library/CloudStorage/OneDrive-Slalom/Training/aoc/2024"
OS_INPUT = os.path.join(ROOT_DIR,"input_files/day3_input.txt")

test_string = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def multiply(x:int, y:int) -> int:
    return x * y

def string_strip(inStr: str) -> int:
    outvals = [int(i) for i in inStr.lstrip("mul(").rstrip(")").split(",")]
    return multiply(outvals[0], outvals[1])

def string_find(inStr: str, proc_state = True) -> int:
    mul_list = re.findall("mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)",inStr)
    return mul_list

def proc_list(inList: list) -> int:
    mul_tot = 0
    if inList is None or inList == []:
        return mul_tot
    proc_state = True
    for mul in inList:
        if mul == "don't()": 
            proc_state = False
            pass
        elif mul == "do()":
            proc_state = True
        elif mul not in ("do()","don't()") and proc_state is True:
            mul_tot += string_strip(mul)
        else:
            pass
    return mul_tot
    #return sum([string_strip(mul) for mul in mul_list])

def main():
    test_tot = string_find(test_string)
    mul_tot, mul_list = 0, []
    proc_state = True
    with open(OS_INPUT) as f:
        for line in f.readlines():
            mul_list.extend(string_find(line))
    


    
    print(proc_list(test_tot))
    print(proc_list(mul_list))
    return mul_tot

if __name__ == "__main__":
    main()