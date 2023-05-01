"""
Find the two values that sum to 2020
return the product of those two values
"""
import itertools


def prod(iter) -> int:
    outProduct = 1
    for i in iter:
        outProduct *= i

outList = []
with open('input.txt') as f:
    for line in f.readlines():
        outList.append(int(line.rstrip()))
tupList = [i for i in itertools.combinations(outList, 3) if sum(i) == 2020]
print(tupList[0][0]*tupList[0][1]*tupList[0][2])


