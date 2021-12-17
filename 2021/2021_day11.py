import numpy as np

def read_input(in_file):
    new_list = []
    with open(in_file, 'r') as f:
        for line in f.readlines():
            new_list.append([int(char) for char in line.rstrip()])
    return np.array(new_list)

def update_array(arr):
    arr += 1
    bloom_tuple = []
    while np.max(arr) > 9:
        bloom = np.where(arr > 9)
        for coord in list(zip(bloom[0], bloom[1])):
            if coord not in bloom_tuple:
                bloom_tuple.append(coord)
            x_dim, y_dim = coord[0], coord[1]
            left = max(0,x_dim-1)
            right = max(0,x_dim+1+1)
            bottom = max(0,y_dim-1)
            top = max(0, y_dim+1+1)
            arr[left:right,bottom:top] += 1
        for coord in bloom_tuple:
            arr[coord[0], coord[1]] = 0
    triggers = len(bloom_tuple)
    print(triggers)
    return arr, triggers



counter = 0
for i in range(100):
    arr, tot = update_array(arr)
    counter += tot

step, tot = 0, 0
while tot < arr.shape[0]*arr.shape[1]:
    step += 1
    arr, tot = update_array(arr)

