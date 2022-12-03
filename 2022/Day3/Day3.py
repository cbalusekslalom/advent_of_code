lowerAlpha = "abcdefghijklmnopqrstuvwxyz"

lowerDict, upperDict  = {}, {}
for i in lowerAlpha:
    lowerDict[i] = lowerAlpha.index(i) + 1
    upperDict[i.upper()] = lowerDict[i] + 26


def list_comp(lst1, lst2) -> str:
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def list_create(inpStr: str):
    strMidway = int(len(inpStr)/2)
    strList = [i for i in inpStr]
    lst1 = strList[:strMidway]
    lst2 = strList[strMidway:]
    return lst1, lst2


with open('input.txt') as f:
    elf_dict = {}
    counter = 0
    key_counter = 0
    for line in f.readlines():
        if key_counter not in elf_dict.keys():
            elf_dict[key_counter] = []
        elf_dict[key_counter] += [line.rstrip()]
        counter += 1
        if counter % 3 == 0:
            key_counter += 1
            counter = 0
    print(elf_dict)

luggageTotal = 0
for key, value in elf_dict.items():
    commonChar = list_comp(list_comp(value[0], value[1]),value[2])[0]
    if commonChar in lowerDict:
        charVal = lowerDict[commonChar]
    elif commonChar in upperDict:
        charVal = upperDict[commonChar]
    else:
        charVal = 0
    print(commonChar, charVal)
    luggageTotal += charVal
print(luggageTotal)
"""
luggageTotal = 0
charVal = 0
lst1, lst2 = list_create(line.rstrip())
commonChar = list_comp(lst1, lst2)[0]
if commonChar in lowerDict:
    charVal = lowerDict[commonChar]
elif commonChar in upperDict:
    charVal = upperDict[commonChar]
else:
    charVal = 0
print(commonChar, charVal)
luggageTotal += charVal
print(luggageTotal)
"""