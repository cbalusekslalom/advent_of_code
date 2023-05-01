
class Valve:

    def __init__(self, name, flowrate, children = None):
        self.name = name
        self.flowrate = flowrate
        self.openTime = 0
        self.children = []

    def add_children(self, inList):
        assert isinstance(inList, list)
        if len(inList) == 0:
            print("invalid input.  provide at least one input")
        for child in inList:
            self.children.append(child)

    def get_flowrate(self):
        return self.flowrate

    def set_openTime(self, minute):
        self.openTime = minute

    def get_total_flow(self):
        if self.openTime > 0:
            return (30-self.openTime)*self.flowrate
        return 0



def add_vertex(v):
    global graph
    global vertices_no
    if v in graph:
        print("Vertex already exists")
    else:
        vertices_no += 1
        graph[v] = []

def add_edge(v1, v2, weight):
    global graph
    if v1 not in graph:
        print(f"{v1} not found in graph")
    elif v2 not in graph:
        print(f"{v2} not found in graph")
    else:
        temp_list = [v2, weight]
        graph[v1].append(temp_list)

