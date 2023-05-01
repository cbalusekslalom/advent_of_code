import ast
from collections import defaultdict


def read_infile_pt1(inFile):
    outputDict = {}
    key_counter = 1
    with open(inFile) as f:
        for line in f.readlines():
            if key_counter not in outputDict.keys():
                outputDict[key_counter] = {}
            if line.rstrip() == '':
                key_counter += 1
                continue
            if outputDict[key_counter] == {}:
                outputDict[key_counter][1] = ast.literal_eval(line.rstrip())
            else:
                outputDict[key_counter][2] = ast.literal_eval(line.rstrip())
    return outputDict


def read_infile_pt2(inFile):
    outputDict = {}
    key_counter = 1
    with open(inFile) as f:
        for line in f.readlines():
            if key_counter not in outputDict.keys():
                outputDict[key_counter] = {}
            if line.rstrip() == '':
                continue
            else:
                outputDict[key_counter] = ast.literal_eval(line.rstrip())
                key_counter += 1
    print(key_counter)
    outputDict[key_counter] = [[2]]
    key_counter += 1
    outputDict[key_counter] = [[6]]
    return outputDict


def compare_int(left: int, right: int) -> bool:
    if left > right:
        return False
    elif left < right:
        return True
    else:
        return None


def compare(left, right) -> bool:
    if type(left) == list and type(right) == list:
        if len(left) == 0 and len(right) > 0:
            return True
        elif len(left) > 0 and len(right) == 0:
            return False
        #print('list list compare')
        for elem in range(min(len(left), len(right))):
            if type(left[elem]) == list or type(right[elem]) == list:
                #print('calling recursion')
                if compare(left[elem], right[elem]) is not None:
                    return compare(left[elem], right[elem])
                    break
            else:
                if compare_int(left[elem], right[elem]) is not None:
                    return compare_int(left[elem], right[elem])
                    break
        if len(left) > len(right):
            return False
        elif len(left) < len(right):
            return True
    elif type(left) == int and type(right) == list:
        #print('int list compare')
        left_list = [left]
        return compare(left_list, right)
    elif type(right) == int and type(left) == list:
        #print('list int compare')
        right_list = [right]
        return compare(left, right_list)
    elif type(left) == int and type(right) == int:
        return compare_int(left, right)


def swap(list, in1, in2):
    list[in1], list[in2] = list[in2], list[in1]
    return list

### compare position i with i+1
### if i > i+ 1 swap, else i is < i+ 1 so start with i-1 and reverse
### if start_ind = 0 again, then set true, start with 1 (i+ 1) and forward direction


def bubble_sort(array, dictionary):
    n = len(array)

    for i in range(n):
        already_sorted = True

        for j in range(n - i - 1):
            if not compare(dictionary[array[j]], dictionary[array[j + 1]]):
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False

        if already_sorted:
            break

    return array


## print(read_infile('test_input.txt'))
### Recursive function to build and check lists


def main():
    # inputDict = read_infile_pt1('test_input.txt')
    inputDict2 = read_infile_pt2('input.txt')
    keyList = [key for key in inputDict2]
    # orderCounter = 0
    """for key, value in inputDict.items():
        print(key)
        print(value)
        comparison = compare(value[1], value[2])
        if comparison:
            orderCounter += key
        print(comparison)
    print(orderCounter)"""
    orderList = bubble_sort(keyList, inputDict2)

    for idx, i in enumerate(orderList):
        #print(i, orderList[idx])
        #print(inputDict2[i], '\n', inputDict2[orderList[idx]])
        if idx == len(orderList) - 1:
            break
        if not compare(inputDict2[i], inputDict2[orderList[idx+1]]):
            print('!!!unequal')

    print([(idx, inputDict2[val]) for idx, val in enumerate(orderList)])
    print(orderList.index(301), orderList.index(302))
    print(inputDict2[301], inputDict2[302])



if __name__ == '__main__':
    main()
