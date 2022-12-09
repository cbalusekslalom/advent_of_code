"""
[-2,2]  [-1,2]  [0,2]   [1,2]   [2,2]
[-2,1]                          [2,1]
[-2,0]          [0,0]           [2,0]
[-2,-1]                         [2,-1]
[-2,-2] [-1,-2] [0,-2]  [1,-2]  [2,-2]
"""



def read(inputFile):
    outList = []
    with open(inputFile) as f:
        for line in f.readlines():
            dir, mag = line.rstrip().split()[0], line.rstrip().split()[1]
            outList.append((dir, mag))
    return outList


class Head_tail:
    def __init__(self, n):
        self.n = n
        self.tail_dict = {i: (0, 0) for i in range(self.n)}
        self.tail_list_dict = {i: [self.tail_dict[i]] for i in self.tail_dict.keys()}
        self.head_position = (0, 0)
        self.head_list = [self.head_position]

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
            self.tail_dict[0] = self.head_position
            self.tail_list_dict[0].append(self.head_position)
            for i in range(1,self.n):
                self.tail_check(i)
        print(f"moved {dir} for {mag} steps {[self.tail_dict[i] for i in range(self.n)]}.")

    def get_tail_position(self, ind, int):
        return self.tail_dict[ind][int]

    def tail_check(self, ind):
        self.x_diff = self.get_tail_position(ind-1, 0) - self.get_tail_position(ind, 0)
        self.y_diff = self.get_tail_position(ind-1, 1) - self.get_tail_position(ind, 1)
        if [self.x_diff, self.y_diff] in [[1, 2], [2, 1], [2, 2]]:
            self.tail_dict[ind] = (self.tail_dict[ind][0]+1, self.tail_dict[ind][1]+1)
        elif [self.x_diff,self.y_diff] in [[-1, 2], [-2, 1], [-2, 2]]:
            self.tail_dict[ind] = (self.tail_dict[ind][0]-1, self.tail_dict[ind][1]+1)
        elif [self.x_diff,self.y_diff] in [[-1, -2], [-2, -1], [-2, -2]]:
            self.tail_dict[ind] = (self.tail_dict[ind][0]-1, self.tail_dict[ind][1]-1)
        elif [self.x_diff, self.y_diff] in [[1, -2], [2, -1], [2, -2]]:
            self.tail_dict[ind] = (self.tail_dict[ind][0] + 1, self.tail_dict[ind][1] - 1)
        elif abs(self.x_diff) == 2:
            self.tail_dict[ind] = (self.tail_dict[ind][0] + int(self.x_diff/2), self.tail_dict[ind][1])
        elif abs(self.y_diff) == 2:
            self.tail_dict[ind] = (self.tail_dict[ind][0], self.tail_dict[ind][1] + int(self.y_diff/2))
        else:
            self.tail_dict[ind] = self.tail_dict[ind]
        self.tail_list_dict[ind].append(self.tail_dict[ind])

    def unique_positions(self):
        print(f"the number of unique tail positions is {[len(set(self.tail_list_dict[i])) for i in range(self.n)]}.")


if __name__ == '__main__':
    directions = read('input.txt')
    new_rope = Head_tail()
    for inp in directions:
        new_rope.move(inp[0], int(inp[1]))
    new_rope.unique_positions()
    #print(new_rope.head_list)
    #print(new_rope.tail_list)