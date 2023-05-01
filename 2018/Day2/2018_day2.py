"""Checksum"""
import sys, os


cwd = '/Users/curtis.balusek/Documents/Training/aoc'
inputFile = '2018/Day2/2018_day2_input.txt'

# read in line, split chars for line, dict object for line with letter as key and count


def str_diff(str1: str, str2: str) -> (int, str):
    out_int, letter_same = 0, ''
    if len(str1) != len(str2):
        return -1, ''
    s1 = [l for l in str1]
    s2 = [l for l in str2]
    for ind in range(len(s2)):
        if s2[ind] == s1[ind]:
            letter_same += s2[ind]
        else:
            out_int += 1
    return out_int, letter_same


def letter_dict(input_string: str) -> dict:
    dict_obj = {}
    for letter in input_string:
        if letter not in dict_obj.keys():
            dict_obj[letter] = 1
        else:
            dict_obj[letter] += 1
    return dict_obj


def value_dict(dict_obj: dict) -> dict:
    dict_val = {}
    for value in dict_obj.values():
        if value not in dict_val:
            dict_val[value] = 1
        else:
            dict_val[value] += 1
    return dict_val


def checksum(inline):
    c2, c3 = 0, 0
    new_outdict = value_dict(letter_dict(inline.rstrip()))
    if 2 in new_outdict and new_outdict[2] > 0:
        c2 == 1
    if 3 in new_outdict and new_outdict[3] > 0:
        c3 == 1
    return c2, c3


def main(in_file):
    # two_count, thr_count = 0, 0
    bin_dict = {}
    count2, count3 = 0, 0
    with open(in_file) as f:
        c2, c3 = checksum(in_file)
        count2 += c2
        count3 += c3
        for line in f.readlines():
            bin_dict[line] = []
    for key1 in bin_dict.keys():
        for key2 in bin_dict.keys():
            if key1 == key2:
                continue
            char_diff_total, same_letters = str_diff(key1, key2)
            if char_diff_total == 1:
                print(same_letters)
                return same_letters
    print(checksum)


if __name__ == "__main__":
    main(os.path.join(cwd,inputFile))

