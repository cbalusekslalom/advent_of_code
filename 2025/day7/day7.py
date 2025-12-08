import os, sys 
import operator
from functools import reduce

def find_carat(char_to_find, input_list):
    return [i for i, char in enumerate(input_list) if char == char_to_find]

def read_file(inText):
    file_name = os.path.join(os.getcwd(),'2025/inputs/'+inText)
    beam_dict = {}
    total_beams_split = 0
    total_time_lines = {}
    counter = 0
    with open(file_name, 'r') as f:
        for line in f.readlines():
            counter += 1
            row_check = [idx for idx in line.strip()]
            if 'S' in row_check:
                beam_dict = {idx: 1 if char == 'S' else 0 for idx, char in enumerate(row_check)}
                total_time_lines = {idx: 1 if char == 'S' else 0 for idx, char in enumerate(row_check)}
            if '^' in row_check:
                char_positions = find_carat('^', row_check)
                temp_timeline = {idx:0 for idx in range(len(row_check))}
                for idx in char_positions:
                    if beam_dict[idx] == 1:
                        total_beams_split += 1
                        beam_dict[idx-1] = 1
                        temp_timeline[idx-1] += total_time_lines[idx]
                        beam_dict[idx+1] = 1
                        temp_timeline[idx+1] += total_time_lines[idx]
                #print(f"row: {counter}")
                #print({idx:char for idx, char in enumerate(row_check)})
                #print(total_time_lines)
                #print(temp_timeline)
                total_time_lines.update((idx,0) for idx in char_positions if beam_dict[idx]==1)
                total_time_lines.update((k,v+temp_timeline[k]) for k,v in total_time_lines.items())
                #print(total_time_lines)
                beam_dict.update((idx,0) for idx in char_positions if beam_dict[idx]==1)
    print(total_beams_split)
    print(reduce(operator.add,total_time_lines.values()))
                    