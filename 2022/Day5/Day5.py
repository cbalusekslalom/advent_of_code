"""
have a dictionary of columns 1-9
each one has a list of boxes
for an action, need to move n-many boxes from key ## -> key ##
"""

test_list = {
    1: ['Z', 'N'],
    2: ['M', 'C', 'D'],
    3: ['P']
}

box_list = {
    1: ['N', 'S', 'D', 'C', 'V', 'Q', 'T'],
    2: ['M', 'F', 'V'],
    3: ['F', 'Q', 'W', 'D', 'P', 'N', 'H', 'M'],
    4: ['D', 'Q', 'R', 'T', 'F'],
    5: ['R', 'F', 'M', 'N', 'Q', 'H', 'V', 'B'],
    6: ['C', 'F', 'G', 'N', 'P', 'W', 'Q'],
    7: ['W', 'F', 'R', 'L', 'C', 'T'],
    8: ['T', 'Z', 'N', 'S'],
    9: ['M', 'S', 'D', 'J', 'R', 'Q', 'H', 'N']
}


def string_mod(inpString: str):
    inSplit = inpString.split()
    return int(inSplit[1]), int(inSplit[3]), int(inSplit[5])


def move_boxes(n_many, stack1, stack2):
    numRemove = -1 * n_many
    stack2 += stack1[numRemove:]
    stack1 = stack1[:numRemove]
    return stack1, stack2

inDict = box_list

with open('input.txt') as f:
    n_many = 100
    for line in f.readlines():
        print(line)
        num, fromKey, toKey = string_mod(line)
        print(f"the action to take is {line}.")
        print(f"The number of boxes to move: {num} with starting state:")
        print(f"{fromKey}: {inDict[fromKey]}")
        print(f"{toKey}: {inDict[toKey]}")
        while num > n_many:
            inDict[fromKey], inDict[toKey] = move_boxes(n_many, inDict[fromKey], inDict[toKey])
            num -= n_many
        if num > 0:
            inDict[fromKey], inDict[toKey] = move_boxes(num, inDict[fromKey], inDict[toKey])
        print("processed.  Here's how those boxes look now:")
        print(f"{fromKey}: {inDict[fromKey]}")
        print(f"{toKey}: {inDict[toKey]}")
        """
        moveList = moveList[::-1] when moving 1x1
        print(f"taking from {inDict[fromKey]} and moving to {inDict[toKey]}.")
        print(moveList)

        """

outstring = ""
for key, value in inDict.items():
    outstring += value[-1]
    print(key, value)
print(outstring)








