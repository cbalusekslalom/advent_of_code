import itertools

split_char = '\t'
checksum = 0
second_sum = 0
with open('input.txt') as f:
    for line in f.readlines():
        line_list = [int(i) for i in line.split(split_char)]
        for a, b in itertools.combinations(line_list, 2):
            if a % b == 0 or b % a == 0:
                print(a, b)
                second_sum += max([a, b]) / min([a, b])
        checksum += max(line_list) - min(line_list)


print(f"The checksum is {checksum}")
print(f"The secondary checksum is {second_sum}")
