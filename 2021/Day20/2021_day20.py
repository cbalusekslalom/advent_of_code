"""
read in file
Decoder as list
input image as array (add 10 object buffer?)
convers . -> 0, # -> 1
method that makes duplicate array of zeros and updates based upon input iteration over image

"""
import numpy as np
import matplotlib.pyplot as plt


def read_in_file(in_file):
    array_list = []
    with open(in_file, 'r') as f:
        input_list = [char for char in f.readline().rstrip()]
        input_list = list_to_binary(input_list)
        f.readline()
        for line in f.readlines():
            line_list = [char for char in line.rstrip()]
            binary_list = []
            for item in line_list:
                if item == '.':
                    binary_list.append(0)
                elif item == '#':
                    binary_list.append(1)
            array_list.append(binary_list)
    input_array = np.array(array_list, dtype=int)
    return input_list, input_array


def list_to_binary(input_list):
    bool_list = [0 for i in range(len(input_list))]
    for i, j in enumerate(input_list):
        if j == '.':
            bool_list[i] = 0
        elif j == '#':
            bool_list[i] = 1
        else:
            ValueError()
    return bool_list


def new_image_array(input_array, step):
    x_size, y_size = input_array.shape[0], input_array.shape[1]
    size_increase = 4
    x_size += size_increase
    y_size += size_increase
    if step % 2 == 1:
        new_image = np.zeros((x_size, y_size), dtype=int)
    elif step % 2 == 0:
        new_image = np.ones((x_size, y_size), dtype=int)
    else:
        ValueError()
    for i in range(input_array.shape[0]):
        for j in range(input_array.shape[1]):
            new_image[i+int(size_increase/2)][j+int(size_increase/2)] = input_array[i][j]
    return new_image


def return_new_image(image_array, decoder, step):
    x_size, y_size = image_array.shape[0], image_array.shape[1]
    if step % 2 == 0:
        image_update = np.zeros((x_size, y_size), dtype=int)
    elif step % 2 == 1:
        image_update = np.ones((x_size, y_size), dtype=int)
    else:
        ValueError()
    # go from the row/column just before image to the row/column just after image
    for image_i in range(1, image_update.shape[0]-1):
        for image_j in range(1, image_update.shape[1]-1):
            binary_string = ''
            for update_i in range(image_i-1, image_i+2):
                for update_j in range(image_j - 1, image_j + 2):
                    binary_string += str(image_array[update_i][update_j])
            binary_list_value = int('0b'+binary_string, 2)
            image_update[image_i][image_j] = decoder[binary_list_value]
    return image_update

input_array = np.zeros((5,5), dtype=int)

input_decoder, input_array = read_in_file('2021_day20_input.txt')
for i in range(1,3):
    temp_image = new_image_array(input_array, i)
    input_array = return_new_image(temp_image, input_decoder, i)

