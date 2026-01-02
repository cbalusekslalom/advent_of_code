import os
import re

def read_file(inTxt):
    counter, indicator_dict, sums = 0, {}, 0
    file_name = os.path.join(os.getcwd(), '2025/inputs/'+inTxt)
    with open(file_name, 'r') as f:
        for line in f.readlines():
            buttons = []
            for element in line.split(' '):
                if re.match(r"\[[.#]{,1000}\]", element):
                    on_state = [item for item in list(element) if item not in ['[',']']]
                if re.match(r"\([0-9,]{,1000}\)", element):
                    button = [int(i) for i in list(element) if i not in ['(',',',')']]
                    buttons.append(button)
                if re.match(r"\{[0-9,]{,1000}\}", element):
                    joltage = [item for item in list(element) if item not in ['{','}',',']]
            if counter not in indicator_dict.keys():
                indicator_dict[counter] = Indicator(on_state=on_state, buttons=buttons, joltage=joltage)
            counter += 1
    return indicator_dict

class Button():
    def __init__(self,state,button):
        # if a button is [3], I want to take the state [.....] and make the button [...#.]
        self.button = button 
        self.state = [state[i] if i in button else state[i] for i in range(len(state))]
            

class Indicator():
    def __init__(self, on_state, buttons, joltage):
        self.on_state = on_state
        self.zero_state = [0 for i in range(len(on_state))]
        self.buttons = buttons 
        self.joltage = joltage 
        self.button_map = self.convert_buttons
    @property
    def get_buttons(self):
        return self.button_map
    @property
    def convert_buttons(self):
        counter = 0
        self.button_map = {}
        for button in self.buttons:
            template = [0 for i in range(len(self.on_state))]
            for i in button:
                template[i] = 1
            if counter not in self.button_map.keys():
                self.button_map[counter] = template
            counter += 1
    def button_addition(self, l1, l2):
        outList = []
        for i,j in zip(l1, l2):
            if i == j:
                outList.append(0)
            else:
                outList.append(1)
        return outList
    @property
    def push_buttons(self):
        self.push_counter = 1
        self.out_state = [1 if i == '#' else 0 for i in self.on_state]
        self.outcome_list = [self.button_addition(self.out_state, v) for v in self.button_map.values()]
        while self.zero_state not in self.outcome_list:
            self.push_counter += 1
            self.temp_list = [self.button_addition(tl, v) 
                                 for tl in self.outcome_list 
                                 for v in self.button_map.values() 
                                 if self.button_addition(tl, v) not in self.outcome_list]
            self.outcome_list.extend(self.temp_list)
            if self.push_counter %100 == 0:
                print(f"High push count, {len(self.outcome_list)}")
    @property
    def get_pushes(self):
        if not self.push_counter:
            return 0
        return self.push_counter


counter, button_map = 0, {}
for button in buttons:
    template = [0 for i in range(len(on_state))]
    for i in button:
        template[i] = 1
    if counter not in button_map.keys():
        button_map[counter] = template
    counter += 1