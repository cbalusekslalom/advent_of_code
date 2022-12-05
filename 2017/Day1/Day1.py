
with open('input.txt') as f:
    list_input = [int(i) for i in f.readline()]

sum_total = 0
step = len(list_input)/2
for i in range(-1, len(list_input)-1):
    compare_ind = int((i+step)%len(list_input))
    #print(compare_ind)
    if list_input[i] == list_input[compare_ind]:
        sum_total += list_input[i]
print(sum_total)

