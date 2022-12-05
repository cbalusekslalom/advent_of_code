import itertools

valid_inputs = 0
with open('input.txt') as f:
    for line in f.readlines():
        line_list = line.rstrip().split(' ')
        dup_count = 0
        dup_list = []
        for i in itertools.combinations(line_list, 2):
             if ''.join(sorted(i[0], key=str.lower)) == ''.join(sorted(i[1], key=str.lower)):
             ## PART1 statement if i[0] == i[1]:
                dup_count += 1
                dup_list.append(i[0])
        if dup_count == 0:
            valid_inputs += 1
        #print(dup_count, line, "\t\t", dup_list)
print(valid_inputs)