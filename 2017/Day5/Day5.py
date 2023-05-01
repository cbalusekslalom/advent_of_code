
step_dict = {}
counter = 0
with open('input.txt') as f:
    for line in f.readlines():
        step_dict[counter] = int(line.rstrip())
        counter += 1

step_counter = 0
start_pos = 0
while start_pos in step_dict.keys():
    step_counter += 1
    movement = step_dict[start_pos]
    ## part 2
    if movement > 2:
        step_dict[start_pos] -= 1
    else:
        step_dict[start_pos] += 1
    start_pos += movement
print(step_counter)