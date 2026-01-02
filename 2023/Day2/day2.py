from functools import reduce
import os,sys
from typing import Any

class Game:
    def __init__(self):
        self.draw_dict = {}
        self.draw_ind = 0
        self.red = 0
        self.green = 0
        self.blue = 0
        self.rgb = self.get_rgb()
    def add_draw(self,r,g,b):
        self.draw_dict[self.draw_ind] = Draw(red=r,green=g,blue=b)
        self.draw_ind += 1
    def get_max_draws(self):
        if self.draw_dict == {}:
            pass
        for key, draw in self.draw_dict.items():
            draw_tuple = draw.print_draw()
            if self.red < draw_tuple[0]:
                 self.red = draw_tuple[0]
            if self.green < draw_tuple[1]:
                self.green = draw_tuple[1]
            if self.blue < draw_tuple[2]:
                 self.blue = draw_tuple[2]
    def get_rgb(self):
         self.get_max_draws()
         return [self.red, self.green, self.blue]    

class Draw:
    def __init__(self,red=0,green=0,blue=0):
        self.red = red
        self.green = green
        self.blue = blue
    def print_draw(self):
         return (self.red, self.green, self.blue)
    
def procLine(inLine:str):
    game = inLine.split(": ")[0].split(" ")[1]
    draw_dict = procList([x.split(', ') for x in inLine.split(": ")[1].split("; ")])
    return [int(game), draw_dict]

def procList(inList:list)->dict:
    out_dict, ind = {}, 0
    for item in inList:
        sub_dict = {}
        for items in item:
            splt = items.split(" ")
            sub_dict[splt[1]] = int(splt[0])
        out_dict[ind] = sub_dict
        ind += 1
    return out_dict

def main(input_filename, pt2=False):
    game_dict = {}
    with open(input_filename, 'r') as inFile:
        for line in inFile.readlines():
            game_draws = procLine(line)
            game_dict[game_draws[0]] = Game()
            for draw_val in game_draws[1].values():
                game_dict[game_draws[0]].add_draw(red=draw_val['red'], green=draw_val['green'], blue= draw_val['blue'])
            game_dict.get_rgb()
    ## Hard coding values
    rgb_m = [12, 13, 14]
    total_game_sum = 0
    power_sum = 0
    for game in game_dict.keys():
        game_rgb = game_dict[game].get_rgb()
        if all(x >= y for x,y in zip(rgb_m, game_rgb)):
            total_game_sum += game
        power_sum += reduce((lambda x, y: x*y), game_rgb)
    print(f"The total of all workign games is: {total_game_sum}")
    print(f"The power sum of rgb games is {power_sum}")



    ## dictionary of games 