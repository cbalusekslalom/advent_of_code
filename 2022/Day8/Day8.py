import numpy as np

test_arr = np.array([[3,0,3,7,3],[2,5,5,1,2],[6,5,3,3,2],[3,3,5,4,9],[3,5,3,9,0]])

def read_file(inFile):
    matrix_a = []
    print("opening file")
    with open(inFile) as f:
        for line in f.readlines():
            matrix_a.append([int(i) for i in line.rstrip()])
    return np.array(matrix_a)

### pt1
def top(arr, pos) -> bool:
    pos_row, pos_col = pos[0], pos[1]
    for j in arr[0:pos_row, pos[1]]:
        if j >= arr[pos]:
            return False
    return True


def bottom(arr, pos):
    pos_row, pos_col = pos[0], pos[1]
    for j in arr[pos_row+1:len(arr), pos[1]][::-1]:
        if j >= arr[pos]:
            return False
    return True


def left(arr, pos):
    pos_row, pos_col = pos[0], pos[1]
    for j in arr[pos_row, 0:pos_col]:
        if j >= arr[pos]:
            return False
    return True


def right(arr, pos):
    pos_row, pos_col = pos[0], pos[1]
    for j in arr[pos_row, pos_col+1:len(arr)][::-1]:
        if j >= arr[pos]:
            return False
    return True

#############
## pt2
#############


def top_count(arr, pos) -> int:
    pos_row, pos_col = pos[0], pos[1]
    counter = 0
    if pos_col == 0:
        return 0
    print(arr[0:pos_row, pos[1]][::-1])
    for j in arr[0:pos_row, pos[1]][::-1]:
        if j >= arr[pos]:
            counter += 1
            break
        counter += 1
    return counter


def bottom_count(arr, pos) -> int:
    pos_row, pos_col = pos[0], pos[1]
    counter = 0
    if pos_row == len(arr)-1:
        return 0
    print(arr[pos_row+1:len(arr), pos[1]])
    for j in arr[pos_row+1:len(arr), pos[1]]:
        if j >= arr[pos]:
            counter += 1
            break
        counter += 1
    return counter


def left_count(arr, pos) -> int:
    pos_row, pos_col = pos[0], pos[1]
    counter = 0
    if pos_col == 0:
        return 0
    print(arr[pos_row, 0:pos_col][::-1])
    for j in arr[pos_row, 0:pos_col][::-1]:
        if j >= arr[pos]:
            counter += 1
            break
        counter += 1
    return counter


def right_count(arr, pos) -> int:
    pos_row, pos_col = pos[0], pos[1]
    counter = 0
    if pos_col == len(arr) - 1:
        return 0
    for j in arr[pos_row, pos_col+1:len(arr)]:
        if j >= arr[pos]:
            counter += 1
            break
        counter += 1
    return counter


def get_tree_count(arr, pos) -> int:
    return top_count(arr, pos) * bottom_count(arr, pos) * left_count(arr, pos) * right_count(arr, pos)


def get_count(inList) -> int:
    counter = 0
    for idx, x in np.ndenumerate(inList):
        if top(inList, idx) or bottom(inList, idx) or left(inList, idx) or right(inList, idx):
            counter += 1

    return counter


def rotate_matrix(inMat):
    return list(zip(*inMat))[::-1]


def main():
    new_matrix = read_file('input.txt')
    #new_matrix = np.array([[3, 0, 3, 7, 3], [2, 5, 5, 1, 2], [6, 5, 3, 3, 2], [3, 3, 5, 4, 9], [3, 5, 3, 9, 0]])
    print(len(new_matrix), len(new_matrix[0]))
    #print(f"the matrix has {get_count(new_matrix)} many visible trees.")
    print(max([get_tree_count(new_matrix, idx) for idx, x in np.ndenumerate(new_matrix)]))



if __name__ == "__main__":
    main()
