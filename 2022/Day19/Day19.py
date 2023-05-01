
def open_blueprints(inputFile):
    blueprint_dict = {}
    with open(inputFile) as f:
        for line in f.readlines():
            ls1 = line.split(': ')
            name = int(ls1[0].split(' ')[1])
            ingredients = ls1[1].split(". ")
            print(ingredients)
            ing_list = []
            for ing in ingredients:
                ing = ing.split(' ')
                if len(ing) == 6:
                    ing_list.append(int(ing[4]))
                if len(ing) == 9:
                    ing_list.append((int(ing[4]), int(ing[7])))
            blueprint_dict[name] = Blueprint(name, ing_list[0], ing_list[1], ing_list[2], ing_list[3])
    return blueprint_dict


class Blueprint:
    def __init__(self, name, ore_cost, clay_cost, obsidian_cost, geode_cost):
        self.number = name
        self.ore_cost = ore_cost
        self.clay_cost = clay_cost
        self.obsidian_ore_cost = obsidian_cost[0]
        self.obsidian_clay_cost = obsidian_cost[1]
        self.geode_ore_cost = geode_cost[0]
        self.geode_obs_cost = geode_cost[1]
        self.ore, self.clay, self.obsidian, self.geode = 0, 0, 0, 0
        self.add_geode_robot, self.add_obsidian_robot, self.add_clay_robot, self.add_ore_robot = False, False, False, False
        self.ore_robot, self.clay_robot, self.obsidian_robot, self.geode_robot = 1, 0, 0, 0
        self.minute = 0

        print(f"Blueprint {self.number}: Ore {self.ore_cost}, \
         Clay {self.clay_cost}, Obs {self.obsidian_ore_cost} ore and {self.obsidian_clay_cost} clay, \
         and Geode {self.geode_ore_cost} ore and {self.geode_obs_cost} obs.")
    def make_robot(self):
        if self.ore >= self.geode_ore_cost and self.obsidian >= self.geode_obs_cost:
            self.add_geode_robot = True
            self.ore -= self.geode_ore_cost
            self.obsidian -= self.geode_obs_cost
        if self.ore >= self.obsidian_ore_cost and self.clay >= self.obsidian_clay_cost:
            self.add_obsidian_robot = True
            self.ore -= self.obsidian_ore_cost
            self.clay -= self.obsidian_clay_cost
        if self.ore >= self.clay_cost:
            if self.clay_robot > self.obsidian_clay_cost or self.clay_robot + self.clay > self.obsidian_clay_cost:
                pass
            else:
                self.add_clay_robot = True
                self.ore -= self.clay_cost
        if self.ore >= self.ore_cost:
            if self.ore_robot > max(self.obsidian_ore_cost, self.geode_ore_cost, self.clay_cost, self.ore_cost):
                pass
            self.add_ore_robot = True
            self.ore -= self.ore_cost
        else:
            pass
    def add_robot(self):
        if self.add_ore_robot:
            self.ore_robot += 1
            self.add_ore_robot = False
        if self.add_clay_robot:
            self.clay_robot += 1
            self.add_clay_robot = False
        if self.add_obsidian_robot:
            self.obsidian_robot += 1
            self.add_obsidian_robot = False
        if self.add_geode_robot:
            self.geode_robot += 1
            self.add_geode_robot = False
    def pass_time(self):
        self.make_robot()
        self.ore += self.ore_robot
        self.clay += self.clay_robot
        self.obsidian += self.obsidian_robot
        self.geode += self.geode_robot
        self.add_robot()
        self.minute += 1
    def get_robots(self):
        print(f"Currently have {self.ore_robot} ore robots, {self.clay_robot} clay robots, \
{self.obsidian_robot} obsidian robots, and {self.geode_robot} geode robots.")
    def get_materials(self):
        print(f"Currently have {self.ore} ore, {self.clay} clay, \
        {self.obsidian} obsidian, and {self.geode} geode.")


def main():
    new_blueprints = open_blueprints("test_input.txt")
    minute = 1
    for key in new_blueprints.keys():
        print(f"starting blueprint {key}.")
        minute = 1
        while minute < 25:
            print(f"minute {minute}")
            new_blueprints[key].pass_time()
            new_blueprints[key].get_robots()
            new_blueprints[key].get_materials()
            minute += 1
        print("completed \n")


if __name__ == "__main__":
    main()

