"""
Simulating Lantern Fish
Need to create a day method
Need to create a lantern fish class
"""

def read_input_file(inp_text: str) -> list:
    return [int(i) for i in open(inp_text,'r').readline().split(',')]


def make_dict(inp: int):
    new_dict = {}
    for i in range(inp):
        new_dict[i] = 0
    return new_dict


class LanternFish():
    """This class generates a laternfish then updates it's time to create more lantern fish"""

    def __init__(self, new_age=8, day_born=0):
        self.age = new_age
        self.dob = day_born

    def update_day(self):
        if self.age == 0:
            self.age = 6
        else:
            self.age -= 1


def main(inp_file, days):
    # read in file
    # create new dictionary of lanternfish
    # 'aoc_2021_day6_test.txt'
    # counter, daytime = 0, 0
    # lantern_dict = {}
    new_inp_list = read_input_file(inp_file)
    """
    for inp in new_inp_list:
        lantern_dict[counter] = LanternFish(inp, 0)
        counter += 1
    """
    old_fish, new_fish = [0 for i in range(7)], [0 for i in range(9)]
    for inp in new_inp_list:
        old_fish[inp] += 1

    today = 0
    while today < days:
        fish_spawned = old_fish.pop(0) + new_fish.pop(0)
        old_fish.append(fish_spawned)
        new_fish.append(fish_spawned)
        today += 1

    old_sum, new_sum = 0, 0
    for i in old_fish:
        old_sum += i
    for j in new_fish:
        new_sum += j

    print(f'the sum of fish created is: {old_sum + new_sum}')
    """
    while daytime < days:
        temp_dict = {}
        for key in lantern_dict.keys():
            if lantern_dict[key].age == 0:
                temp_dict[counter] = LanternFish()
                counter += 1
            else:
                pass
            lantern_dict[key].update_day()
        lantern_dict.update(temp_dict)
        daytime += 1

    print(len(lantern_dict))
    """
