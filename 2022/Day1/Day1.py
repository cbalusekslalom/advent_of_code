"""
Given a file with [numeric input OR empty] line.
If Line is Empty, denotes new elf.
Else, SUM ints for total value of elf.

PART1:
Create a dictionary of Elves and attribute total value of each elf.
Sort Dictionary and get 1st input

PART2:
Get first 3 elements of Sorted dictionary and SUM.

"""
import collections


def create_elf_gl(InputFile: str) -> dict:
    counter = 0
    out_dict = {counter: 0}
    with open(InputFile) as f:
        for line in f.readlines():
            if line.strip() == '':
                counter += 1
                out_dict[counter] = 0
            else:
                out_dict[counter] += int(line.strip())
    return out_dict

elf_dict = create_elf_gl('input.txt')

### PART1: Reverse Sort dictionary

print(dict(sorted(elf_dict.items(), key=lambda item: item[1], reverse=True)))

### PART2: Get TOP 3 elves.

total_top3 = 0
for tup in collections.Counter(elf_dict).most_common(3):
    total_top3 += tup[1]
print(total_top3)

print(sum([tup[1] for tup in collections.Counter(elf_dict).most_common(3)]))
