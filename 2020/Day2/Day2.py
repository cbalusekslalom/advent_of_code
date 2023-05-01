

def check_valid(range, letter, string):
    count_of_letter = len([i for i in string if i == letter[0]])
    if count_of_letter < int(range.split('-')[0]) or count_of_letter > int(range.split('-')[1]):
        return False
    return True


with open('input.txt') as f:
    counter = 0
    for line in f.readlines():
        lineList = line.split(' ')
        range, letter, string = lineList[0], lineList[1], lineList[2]
        if check_valid(range, letter, string):
            counter += 1
print(counter)
