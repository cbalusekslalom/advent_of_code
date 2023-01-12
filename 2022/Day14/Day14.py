import ast


def unique_list(inpList):
    unique_list = []
    for x in inpList:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list


def getTuples(tup1, tup2):
    tupList = []
    if tup1[0] == tup2[0]:
        for i in range(min(tup1[1],tup2[1]),max(tup1[1],tup2[1])+1):
            tupList.append((tup1[0], i))
    elif tup1[1] == tup2[1]:
        for i in range(min(tup1[0],tup2[0]),max(tup1[0],tup2[0])+1):
            tupList.append((i, tup1[1]))
    return tupList


def sand_drop(pos: tuple, block_list, min_max_tup):
    if pos[0] < min_max_tup[0] or pos[0] > min_max_tup[1]:
        return False
    if (pos[0], pos[1]+1) not in block_list:
        sand_drop((pos[0], pos[1]+1), block_list)
    elif (pos[0]-1, pos[1]+1) not in block_list:
        sand_drop((pos[0]-1, pos[1]+1), block_list)
    elif (pos[0] + 1, pos[1] + 1) not in block_list:
        sand_drop((pos[0] + 1, pos[1] + 1), block_list)
    else:
        block_list.append(pos)
    return block_list



min_x, max_x, min_y, max_y = 492, 493, 145, 146
with open('input.txt') as f:
    list_of_tuples = []
    for line in f.readlines():
        inpList = [ast.literal_eval(inp) for inp in line.split(' -> ')]
        for indx in range(1, len(inpList)):
            min_x, max_x = min(min_x, inpList[indx][0]), max(max_x, inpList[indx][0])
            min_y, max_y = min(min_y, inpList[indx][1]), max(max_y, inpList[indx][1])
            list_of_tuples.append(getTuples(inpList[indx-1], inpList[indx]))

tupleList = unique_list([(x[0], x[1]) for l in list_of_tuples for x in l])
print(min_x, max_x, min_y, max_y)

print(tupleList)

valid = True
while valid:
    sand_drop((500,0), tupleList)
