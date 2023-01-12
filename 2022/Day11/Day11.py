import json

class Monkey:

    def __init__(self, id):
        self.id = id
        self.item_list = []
        self.operation_int = 0
        self.true_monkey = 0
        self.false_monkey = 0

    def set_operation_int(self, intgr):
        self.operation_int = intgr

    def set_item_list(self, inList):
        self.item_list = inList

    def get_item_list(self):
        return self.item_list

    def set_true_monkey(self, id):
        self.true_monkey = id

    def set_false_monkey(self, id):
        self.false_monkey = id

    def item_operation(self, item):
        return floor(item*self.operation_int/3)

    def test_operation(self, item):
        if item == 0:
            return True


def openFile(inputFile):
    with open(inputFile) as f:
        outObj = {}
        counter = 0
        for line in f.readlines():
            if counter not in outObj.keys():
                outObj[counter] = {}
            if line.rstrip() == '':
                counter += 1
                continue
            outObj[counter][line.split(':')[0]] = line.split(':')[1]
    return outObj


with open('input.txt') as f:
    outObj = {}
    counter = 0
    for line in f.readlines():
        if counter not in outObj.keys():
            outObj[counter] = {}
        if line.rstrip() == '':
            counter += 1
            continue
        if line.strip().split()[0] == 'Monkey':
            monkNum = line.strip().split()[1][0]
            outObj[counter] = Monkey(monkNum)
        elif line.strip().split()[0] == 'Starting':
            outObj[counter].item_list = [int(i) for i in line.strip().split(':')[1].strip().split(', ')]
        elif line.strip().split([0]) == 'Operation':

    print(outObj)