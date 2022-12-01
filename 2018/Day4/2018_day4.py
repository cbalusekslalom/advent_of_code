"""
track the guards
"""
from datetime import datetime

class Guard():
    '''Class to keep track of guard's sleep time'''
    def __init__(self, number):
        self.number = number
        self.sleep_total = 0
        self.sleep_list = []

    def add_sleep(self, start, end):
        self.sleep_list.append([start, end])
        self.sleep_total += (end - start)


def read_input(in_file):
    with open(in_file, 'r') as f:
        time_list = [line.rstrip() for line in f.readlines()]
    time_list.sort()
    return time_list

in_file = '2018_day4_input.txt'

time_list = read_input(in_file)
guard_dict = {}
while len(time_list) > 0:
    inp = time_list.pop(0)
    inp_list = re.split(r"\[(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2})\]\s([a-zA-Z\s#0-9]*)", inp)
    inp_list = [x for x in inp_list if x != '']
    if 'Guard' in inp_list[1]:
        guard_num = inp_list[1].split(' ')[1]
        if guard_num not in guard_dict:
            guard_dict[guard_num] = Guard(guard_num)
        start_wake_time = inp_list[0]