def read(inputFile):
    outList = []
    with open(inputFile) as f:
        for line in f.readlines():
            dir, mag = line.rstrip().split()[0], line.rstrip().split()[1]
            outList.append((dir, mag))
    return outList


class Head_tail:
    def __init__(self):
        self.start = (0, 0)
        self.head_position = (0, 0)
        self.tail_position = (0, 0)
        self.head_list = [self.head_position]
        self.tail_list = [self.tail_position]
    def move(self, dir, mag):
        for m in range(mag):
            if dir == 'L':
                self.head_position = (self.head_position[0]-1, self.head_position[1])
            if dir == 'R':
                self.head_position = (self.head_position[0]+1, self.head_position[1])
            if dir == 'U':
                self.head_position = (self.head_position[0], self.head_position[1]+1)
            if dir == 'D':
                self.head_position = (self.head_position[0], self.head_position[1]-1)
            self.head_list.append(self.head_position)
            self.tail_check()
        print(f"moved {dir} for {mag} steps {self.head_position}, {self.tail_position}.")
    def get_head_position(self,int):
        return self.head_position[int]
    def get_tail_position(self,int):
        return self.tail_position[int]
    def tail_check(self):
        self.x_diff = self.get_head_position(0) - self.get_tail_position(0)
        self.y_diff = self.get_head_position(1) - self.get_tail_position(1)
        if [self.x_diff, self.y_diff] in [[1,2],[2,1]]:
            self.tail_position = (self.tail_position[0]+1, self.tail_position[1]+1)
        elif [self.x_diff,self.y_diff] in [[-1,2],[-2,1]]:
            self.tail_position = (self.tail_position[0]-1, self.tail_position[1]+1)
        elif [self.x_diff,self.y_diff] in [[-1,-2],[-2,-1]]:
            self.tail_position = (self.tail_position[0]-1, self.tail_position[1]-1)
        elif [self.x_diff, self.y_diff] in [[1, -2], [2, -1]]:
            self.tail_position = (self.tail_position[0] + 1, self.tail_position[1] - 1)
        elif abs(self.x_diff) == 2:
            self.tail_position = (self.tail_position[0] + int(self.x_diff/2), self.tail_position[1])
        elif abs(self.y_diff) == 2:
            self.tail_position = (self.tail_position[0], self.tail_position[1] + int(self.y_diff/2))
        else:
            self.tail_position = self.tail_position
        self.tail_list.append(self.tail_position)
    def unique_positions(self):
        #print(f"the number of unique head positions is {self.head_list}.")
        print(f"the number of unique tail positions is {len(set(self.tail_list))}.")


if __name__ == '__main__':
    directions = read('input.txt')
    new_rope = Head_tail()
    for inp in directions:
        new_rope.move(inp[0], int(inp[1]))
    new_rope.unique_positions()
    #print(new_rope.head_list)
    #print(new_rope.tail_list)