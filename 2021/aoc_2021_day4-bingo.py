"""
Playing bingo
Create class of bingo_card (nxn array with input)
Create function that can mark the array
Create function to return the 'score' (unmarked values)
"""
import numpy as np


def read_input_into_bingo(inp_text: str):
    # do two things and return
    # 1st, string of input
    # list of arrays
    with open(inp_text, 'r') as in_file:
        string_inp = [int(i) for i in in_file.readline().split(',')]
        in_file.readline()
        lines = [line.rstrip() for line in in_file]
    proc = True
    bingo_card_num = 1
    bingo_dict = {}
    new_arr = []
    while proc:
        inp_list = lines.pop(0)
        if inp_list == '':
            continue
        else:
            new_arr.append([int(i) for i in inp_list.split()])
        if len(new_arr) == 5:
            bingo_dict[bingo_card_num] = new_arr
            bingo_card_num += 1
            new_arr = []
        if len(lines) < 1:
            proc = False
    return string_inp, bingo_dict


class BingoCard:
    """This class should create a bingo card from an input_array"""

    # number dict is going to take the array input and map a value to a location in card (i, j)
    # card is an array of all Os that will be transformed to X by lookup in number dict
    def __init__(self, name, inp_array):
        self.name = name
        self.number_list = [j for i in inp_array for j in i]
        self.number_dict = {key: value for key, value in list(zip(self.number_list,[[i,k] for i,j in enumerate(inp_array) for k,m in enumerate(j)]))}
        self.card_val = inp_array
        self.card = [['O'] * 5 for ind in range(5)]
        self.score = sum([i for i in self.number_list])
        self.is_bingo = False

    def check_bingo(self):
        for i in self.card:
            if 'O' not in i:
                self.is_bingo = True
            else:
                continue
        for j in np.transpose(self.card):
            if 'O' not in j:
                self.is_bingo = True
            else:
                continue

    def print_card(self):
        for s in self.card_val:
            print(*s)

    def card_score(self):
        self.score = sum([i for i in self.number_list])
        print(f"THE CARD {self.name} IS A WINNER!")
        return [f"The card score is {self.score}"]

    def card_update(self, num):
        if num in self.number_dict.keys():
            row, col = self.number_dict[num][0], self.number_dict[num][1]
            self.number_list.remove(num)
            self.number_dict.pop(num)
            self.card[row][col] = 'X'
            self.card_val[row][col] = 'X'
        self.check_bingo()
        if self.is_bingo:
            print(self.card_score())

def main():
    bingo_numbers, bingo_dictionary = read_input_into_bingo('aoc_2021_day4_input.txt')
    card_status = {}
    for key in bingo_dictionary.keys():
        bingo_dictionary[key] = BingoCard(key, bingo_dictionary[key])
    list_of_winners = []
    list_of_keys = list(bingo_dictionary)
    print(f"The number drawn is {inp}")
    for key in list_of_keys:
        for inp in bingo_numbers:
            card_no = bingo_dictionary[key]
            bingo_dictionary[key].card_update(inp)
            if bingo_dictionary[key].is_bingo:
                card_status[key] = bingo_numbers.index(inp)
                print(bingo_numbers.index(inp), card_no.name, inp, card_no.score)
                break
                # bingo_dictionary[key].print_card()
                # list_of_winners.append([key, inp, bingo_dictionary[key].score])

        print(f"the remaining cards are: {list_of_keys}")
        if len(list_of_keys) == 0:
            break
    print(list_of_winners)


