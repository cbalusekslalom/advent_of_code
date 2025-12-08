import os, sys
#import utils.helpers

ROOT_PATH = '/Users/curtisbalusek/Library/CloudStorage/OneDrive-Slalom/Training/aoc/2024'

def distance(in1:int, in2:int):
    return abs(in1-in2)

def make_dict(l1:list, l2:list)->dict:
    out_dict = {}
    out_dict = {key:l2.count(key) for key in l1 if key not in out_dict}
    return out_dict

def similarity(l1:list, l2:list) -> int:
    total_similarity = 0
    input_dict = make_dict(l1, l2)
    for i in range(len(l1)):
        total_similarity += l1[i]*input_dict[l1[i]]
    return total_similarity

def read_file(path_to_file):
    l1, l2 = [], []
    with open(os.path.join(ROOT_PATH,path_to_file)) as f:
        for line in f.readlines():
            out = line.strip().split('   ')
            l1.append(int(out[0]))
            l2.append(int(out[1]))
        return l1, l2
    
def main():
    total_distance = 0
    left, right = read_file('input_files/day1_input.txt')
    left.sort()
    right.sort()
    for i in range(len(left)):
        total_distance += distance(left[i], right[i])
    print(f"The total_distance is: {total_distance}")
    similar = similarity(left, right)
    print(f"The similarity is: {similar}")

if __name__=='__main__':
    print(main())