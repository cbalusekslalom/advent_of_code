import itertools

input_value = 368078

"""
1,3,5,7,9 & number to fill is always (2k+1)^^2 - (2k-1)^^2
0,0 -> 1 and has 1 space
the level of 1s goes from 1,0 -> 1,1 -> 0,1 -> -1,1 -> -1,0 -> -1,-1 -> 0,-1 -> 1,-1 for #s 2-9
The level of 2s goes from 10 -> 25
The level of 3s goes from 26 -> 50

value will be in the k-th ring
starts at k, -(k-1) and goes around to k, -k for a total of 8k+1 
k = 303

each side is (2k+1)^^2 - (2k-1)^^2 / 4 in length
side = (2k+1)^^2 - (2k-1)^^2 / 4
if input_value < (2k-1)**2 + 4*side:
    one constant is the side length will be k
    just need to find the offset 
"""
k = 0
while input_value > (2*k+1)**2:
    k += 1
side_length = ((2*k+1)**2 - (2*k-1)**2) / 4
side_counter, side_check_bool = 1, True
while side_check_bool:
    if input_value < (2*k-1)**2 + side_counter*side_length:
        side_check_bool = False
        offset = -k + ((2*k-1)**2 + side_counter*side_length - input_value)
    else:
        side_counter += 1

print(k+abs(offset))

### part2
"""
Consider a dictionary of tuples as keys
if key not in dict:
    dict[key] = 0
(0,0) = 1
(1,0) -> (1,1) -> (0,1) -> (-1, 1) -> 
"""
dict_tup = {(0, 0): 1}


def tuple_two_lists(lst1, lst2) -> list:
    outList = []
    for x in lst1:
        for y in lst2:
            outList.append((x, y))
    return outList


def get_neighbors(dic: dict, tple: tuple) -> dict:
    x_val = [tple[0]-1, tple[0], tple[0]+1]
    y_val = [tple[1] - 1, tple[1], tple[1] + 1]
    for tup in tuple_two_lists(x_val, y_val):
        if tup not in dic.keys():
            dic[tup] = 0
    return dic

### Need to think through how to iterate over the coordinate system programatically
### has to do with understanding the counter being less than the max, then going along the perimeter.

m = 0
key_sum = 0
while key_sum < input_value:
    while (2*m+1)**2 < input_value:


