from collections import defaultdict
import re

class Machine():
    def __init__(self, A:list, B:list, Location:list):
        self.pos_x, self.pos_y = 0, 0
        self.button_a_x, self.button_a_y = A[0], A[1]
        self.button_b_x, self.button_b_y = B[0], B[1]
        self.prize_x, self.prize_y = Location[0], Location[1] 
    
    def machine_setup(self):
        print(f"""A: +{self.button_a_x}, +{self.button_a_y}\nB: +{self.button_b_x}, +{self.button_b_y}\nP: {self.prize_x}, {self.prize_y}.""")

    def prize_check(self):
        

## Button A: X+\d{1,}, Y+\d{1,}
## Button B: X+\d{1,}, Y+\d{1,}
## Prize: X=\d{1,}, Y=\d{1,}
    
def read_file(inFile):
    machine_dict = defaultdict()
    counter = 0
    with open(inFile) as f:
        while True:
            lineA = f.readline().rstrip()
            lineB = f.readline().rstrip()
            lineP = f.readline().rstrip()
            print(lineA, lineB, lineP)
            groups = re.match(r'^Button A: X\+(\d{1,}), Y\+(\d{1,})$', lineA)
            A = [int(groups.group(1)), int(groups.group(2))]
            groups = re.search(r'^Button B: X\+(\d{1,}), Y\+(\d{1,})$', lineB)
            B = [int(groups.group(1)), int(groups.group(2))]
            groups = re.search(r'^Prize: X=(\d{1,}), Y=(\d{1,})$', lineP)
            L = [int(groups.group(1)), int(groups.group(2))]
            print(A, B, L)

            if counter not in machine_dict.keys():
                machine_dict[counter] = Machine(A, B, L)
            counter += 1
            line_new = f.readline()
            if line_new == "":
                break
    return machine_dict

if __name__=="__main__":
    md = read_file('input_files/day13_input.txt')
    for key in md.keys():

