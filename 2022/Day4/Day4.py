"""
two lists
range from a-b
if lst1 ^ lst 2 == [lst1 or lst2] then fully contained

"""


def range_builder(inp):
    inp_tup = inp.split('-')
    a,b = int(inp_tup[0]), int(inp_tup[1])
    if a == b:
        return [a]
    return [ i for i in range(a,b+1) ]


with open('input.txt') as f:
    counter_int = 0
    counter_exclusive = 0
    for line in f.readlines():
        line_tups = line.rstrip().split(',')
        lst1, lst2 = range_builder(line_tups[0]), range_builder(line_tups[1])
        intersect = [value for value in lst1 if value in lst2]
        print(intersect)
        if intersect == lst1 or intersect == lst2:
            counter_int += 1
        if len(intersect) > 0:
            counter_exclusive += 1
print(counter_int)
print(counter_exclusive)