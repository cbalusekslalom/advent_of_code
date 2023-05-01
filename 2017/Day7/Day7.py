

class TreeDisc:
    def __init__(self, name, data=None, children=None):
        self.children = []
        self.name = name
        self.data = None
        self.children = []
        self.parent = None
        if children is not None:
            for child in children:
                self.add_child(child)

    def __repr__(self):
        return self.name

    def add_data(self, data):
        self.data = data

    def add_child(self, node):
        assert isinstance(node, TreeDisc)
        self.children.append(node)

    def add_parent(self, node):
        assert isinstance(node, TreeDisc)
        self.parent = node


TreeDict = {}
with open('input.txt') as f:
    for line in f.readlines():
        if len(line.split()) < 3:
            inp = line.split()
            TreeDict[inp[0]] = {'name': inp[0], 'data': inp[1], 'children': None}
        else:
            inp = line.split('->')
            node_property = inp[0].split()
            child_list = [i.strip() for i in inp[1].split(',')]
            TreeDict[node_property[0]] = {'name': node_property[0], 'data': node_property[1], 'children': child_list}

for key, value in TreeDict.items():
    if value['children'] is not None:
        for child in value['children']:
            if type(TreeDict[child]) != TreeDisc:
                TreeDict[child] = TreeDisc(TreeDict[child]['name'], TreeDict[child]['data'], TreeDict[child]['children'])
    if type(value) != TreeDisc:
        TreeDict[key] = TreeDisc(value['name'], value['data'], value['children'])
        if value['children'] is not None:
            for child in value['children']:
                TreeDict[child].add_parent(TreeDict[key])
    else:
        continue

print(TreeDict)