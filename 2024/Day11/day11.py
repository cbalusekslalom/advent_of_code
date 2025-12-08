from functools import reduce
import math 

"""
If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
"""
## we going to map this shit
def map_func(stone: int):
    if stone == 0:
        return (1, None)
    digits = math.floor(math.log10(stone)) + 1
    if digits % 2 == 0: 
        midpt = digits // 2
        tens = 10 ** midpt
        left_stone = stone // tens
        right_stone = stone % tens
        return  (left_stone, right_stone)
    else:
        return (stone*2024, None)
    

def flat_map(f, xs):
    ys = []
    for x in xs:
        ys.extend(f(x))
    return ys

def count_stone_blinks(stone, depth):

    # For this iteration, what is the update for this stone?
    left_stone, right_stone = map_func(stone)

    # Is this the final iteration
    if depth == 1:

        # Final iteration, just count if have one or two stones
        if right_stone is None:
            return 1
        else:
            return 2

    else:

        # Recurse to the next level and add the results if there
        # are two stones
        output = count_stone_blinks(left_stone, depth - 1)
        if right_stone is not None:
            output += count_stone_blinks(right_stone, depth - 1)
        
        return output


def main(inFile, count):
    counter = 0 
    with open(inFile) as f:
        line_list = [int(i) for i in f.readline().split(' ')]
    print(line_list)
    for stone in line_list:
        counter += count_stone_blinks(stone, count)
    print(counter)
    return counter


if __name__=='__main__':
    main('input_files/day11_input.txt', 75)

