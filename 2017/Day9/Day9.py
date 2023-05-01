## recursive function


with open('input.txt') as f:
    inList = [i for i in f.readline()]


def garbage(inputList: list):
    char = inputList.pop(0)
    garbageLine = ''
    while char != '>':
        garbageLine += char
        if char == '!':
            garbageLine += inputList.pop(0)
        char = inputList.pop(0)
    return garbageLine


def whats_in_a_group(inputList: list):
    char = inputList.pop(0)
    group_info = ''
    garbage = ''
    if char == '{':
        group_info += whats_in_a_group(inputList)
    elif char
