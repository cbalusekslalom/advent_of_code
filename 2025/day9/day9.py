import os 

def read_file(inTxt):
    file_name = os.path.join(os.getcwd(), '2025/inputs/'+inTxt)
    tpl_list = []
    with open(file_name, 'r') as f:
        for line in f.readlines():
            tpl_list.append([int(inp) for inp in line.split(',')])
    return tpl_list

def return_area(tpl1, tpl2):
    return abs((tpl2[0]-tpl1[0]-1)*(tpl2[1]-tpl1[1]-1))

