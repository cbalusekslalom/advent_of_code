from collections import defaultdict

class LAN():

    def __init__(self,node1,node2=""):
        self.name = node1
        self.connections = [node2]
    
    def add_cnxn(self,node):
        self.connections.append(node)

    def rm_cnxn(self,node):
        if node in self.connections:
            self.connections.remove(node)
        else:
            print(f"Node; {node} not connected")

def proc_str(inStr):
    nodes = inStr.rstrip().split('-')
    return dict(map(lambda x: (x, [nodes[nodes.index(x) - 1]]), nodes))


lan_dict = defaultdict()
t_list = []
with open('input_files/day23_test.txt') as f:
    for line in f.readlines():
        for n in proc_str(line).keys():
            if n not in lan_dict.keys():
                lan_dict[n] = proc_str(line)[n]
            else: 
                lan_dict[n].extend(proc_str(line)[n])
            if n.startswith('t') and n not in t_list:
                t_list.append(n)
lan_list, t_proc_list = [], []
for t in t_list:
    t_proc_list.append(t)
    for x in lan_dict[t]:
        if x not in t_proc_list:
            paired_list =  [j for j in lan_dict[t] if j in lan_dict[x] and j not in t_proc_list]
            for p in paired_list:
                if [t, p, x] not in lan_list:
                    lan_list.append([t,x,p])    
print(lan_list)
print(len(lan_list))


def key_comp(key1, key2, dic=lan_dict):
    print(key1, key2, dic[key1], dic[key2])
    out_list = [l for l in dic[key1] if l in dic[key2]]
    out_list.extend([key1, key2])
    print(out_list)
    return out_list

def list_comp(l1, l2):
    return [l for l in l1 if l in l2]
#recursively go through each connection 
# for each t_node in our t_list:
# for each node in it's dictionary
# go to each node and add it to the list of participants
# compare against a list of existing connections

def r_fn(key, lan_list = [], dictionary = lan_dict):
    print(f'running for {key}')
    lan_list.append(key)
    sub_list = [j for j in dictionary[key] if j not in lan_list]
    for val in sub_list:
        print(f"running for {val}")
        comp_list = list_comp(sub_list, dictionary[val])
        if comp_list is None:
            print(lan_list)
            return lan_list
        elif len(comp_list) == 1:
            print(lan_list)
            return lan_list.append(val) 
        else:
            for v in comp_list:
                r_fn(v,lan_list=lan_list)

for key, value in lan_dict.items():
    print(f"{key}: {value}")

for t in t_list:
    r_fn(t)

                
            