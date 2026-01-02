import os

def read_file(inTxt):
    file_name = os.path.join(os.getcwd(),'2025/inputs/'+inTxt)
    with open(file_name, 'r') as f:
        return_list = []
        for line in f.readlines():
            return_list.append(line.strip())
        return return_list