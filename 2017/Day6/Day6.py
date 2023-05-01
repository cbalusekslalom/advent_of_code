from collections import defaultdict

inpDict = defaultdict(int)
with open('input.txt') as f:
    inp_list = f.readline().split('\t')
    for i,x in enumerate(inp_list):
        inpDict[i] = int(x)


def get_state(inpDic: dict):
    return [i for i in inpDic.values()]


def distro_nodes(inpDict: dict, start_key: int, nodes: int):
    key_ind = start_key
    inpDict[start_key] = 0
    while nodes > 0:
        key_ind = int((key_ind+1) % 16)
        inpDict[key_ind] += 1
        nodes -= 1
    return inpDict


print(inpDict)
counter = 0
list_of_outcomes = []
m = defaultdict(list)


while get_state(inpDict) not in list_of_outcomes:
    list_of_outcomes.append(get_state(inpDict))
    counter += 1
    min_max_key = min([key for key, value in inpDict.items() if value == max(inpDict.values())])
    inpDict = distro_nodes(inpDict, min_max_key, inpDict[min_max_key])

print(list_of_outcomes.index(get_state(inpDict)))
print(counter)
print(counter - list_of_outcomes.index(get_state(inpDict)))

