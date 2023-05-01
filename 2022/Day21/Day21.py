from functools import reduce

def open_monkey(inputFile):
    outDict = {}
    with open(inputFile) as f:
        for line in f.readlines():
            outDict[line.split(': ')[0]] = line.split(': ')[1]
            if outDict[line.split(': ')[0]] == "root":
                outDict["root"] = outDict["root"][:5] + "==" + outDict["root"][6:]
    return outDict


def dictionary_recursion(inpDict, key):
    if type(inpDict[key]) in [int, float]:
        return inpDict[key]
    yells = inpDict[key].rstrip()
    if '-' in yells:
        return reduce(lambda x, y: x - y, [dictionary_recursion(inpDict, ref) for ref in yells.split(' - ')])
    elif '+' in yells:
        return reduce(lambda x, y: x + y, [dictionary_recursion(inpDict, ref) for ref in yells.split(' + ')])
    elif '*' in yells:
        return reduce(lambda x, y: x * y, [dictionary_recursion(inpDict, ref) for ref in yells.split(' * ')])
    elif '/' in yells:
        return reduce(lambda x, y: x / y, [dictionary_recursion(inpDict, ref) for ref in yells.split(' / ')])
    elif '==' in yells:
        eq = reduce(lambda x, y: x == y, [dictionary_recursion(inpDict, ref) for ref in yells.split(' == ')])
        if eq:
            print(inpDict["humn"])
        else:
            inpDict["humn"] += 1
    else:
        return int(inpDict[key])

def main():
    monkey_dict = open_monkey('input.txt')
    monkey_dict["humn"] = 0
    while
        monkey_dict[key] = dictionary_recursion(monkey_dict, key)
    print(monkey_dict['root'])

if __name__ == "__main__":
    main()
