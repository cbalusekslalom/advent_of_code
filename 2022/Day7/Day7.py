"""
Repo structure
How to build a tree in python

Have some root directory
Starting at root, ls should list the children of a directory



"""
import json

"""
class Tree:
    # use a dictionary to track items by name and values are Directory/File objects
    # pwd is a current state pointer
    def __init__(self):
        self.cwd = Directory('/') # the starting directory
        self.path = self.cwd.get_name()
    def ls(self):
        print(self.cwd.get_children())
    def set_path(self):
        if self.cwd.get_name() == '/':
            self.path = '/'
        else:
            self.path = self.cwd.get_parent() + self.cwd.get_name() + '/'

    def mkdir(self, dir):
        if dir not in self.cwd.children:
            self.cwd.add_child(Directory(dir, [], self.cwd.get_name()))
        else:
            print(f"Directory {dir} already exists.")

    def touch(self, filename, size):
        if filename not in self.cwd.children:
            self.cwd.add_child(File(filename, size, self.cwd.get_name()))

    def cd(self, directory):
        if directory in self.cwd.get_children():
            self.cwd = 
        elif directory == '..':
            self.path = self.dictionary[directory.get_parent()]
        elif directory == '/':
            self.path = self.dictionary[self.root]
        else:
            print("Directory Does Not Exist")
"""


class Directory:
    def __init__(self, name, children=[], parent=None):
        self.name = name ## should be long name to reduce replication /dir1/dir2/dir3
        self.children = children ### should be a list of onjects under this dir
        self.size = 0 ### total size of directory, sum of all children
        self.parent = parent ### filepath of directory above it.
    def get_name(self):
        return self.name
    def add_child(self, child):
        self.children.append(child)
    def get_child(self, childname):
        for child in self.children:
            if child.get_name() == childname:
                return child
    def remove_child(self, child):
        if child in self.get_children():
            self.children.pop(child)
    def get_children(self):
        if not self.children:
            return {}
        return [child.get_name() for child in self.children]
    def print_directory(self):
        self.set_size()
        print(f"{self.name} -> {self.size}.")
        for child in self.children:
            if type(child) == Directory:
                child.print_directory()
            elif type(child) == File:
                pass
                #child.print_file()
            else:
                print("invalid data type")
    def set_size(self):
        self.size = 0
        if not self.children:
            self.size = 0
        else:
            for child in self.children:
                self.size += child.get_size()
    def get_size(self):
        self.set_size()
        return self.size
    def get_desc(self):
        return (self.name, self.get_size())
    def set_parent(self, parent):
        assert isinstance(parent, Directory)
        self.parent = parent
    def get_parent(self):
        return self.parent
    def get_sibling(self):
        self.get_parent().get_children()

class File:
    def __init__(self, name:str, size:int, parent = ''):
        self.name = name
        self.size = size
        self.parent = ''
    def print_file(self):
        print(f"     {self.name} -> {self.size}.")
    def set_name(self, name: str):
        self.name = name
    def get_name(self):
        return self.name
    def set_size(self, size: int):
        self.size = size
    def get_size(self):
        return self.size
    def set_parent(self, parent):
        assert isinstance(parent, Directory)
        self.parent = parent
    def get_parent(self):
        return self.parent

def main():
    cwd = Directory('/')
    cwd.set_parent(cwd)
    counter = 0
    with open('test_input.txt') as f:
        for line in f.readlines():
            counter += 1
            line_list = line.rstrip().split(' ')
            # print(str(counter), [i for i in line_list])
            if line_list[0] == '$':
                if line_list[1] == 'ls':
                    print(cwd.print_directory())
                elif line_list[1] == 'cd':
                    if line_list[2] == '..':
                        cwd = cwd.get_parent()
                        # print(cwd.get_name())
                    elif line_list[2] == '/':
                        while cwd.get_name() != '/':
                            cwd = cwd.get_parent()
                        # print(cwd.get_name())
                    else:
                        print("going into a directory")
                        if line_list[2] in cwd.get_children():
                            cwd = cwd.get_child(line_list[2])
                    print(f"Current Directory: {cwd.get_name()}")
            elif line_list[0] == 'dir':
                cwd.add_child(Directory(line_list[1], [], cwd))
            else:
                cwd.add_child(File(line_list[1], int(line_list[0]), cwd))
    while cwd.get_name() != '/':
        cwd = cwd.get_parent()
    cwd.print_directory()

if __name__ == "__main__":
    main()



"""
class DirectorTree:
    def __init__(self):
        self.root = Directory('/')
        self.current_directory = self.root
        self.path = self.current_directory.get_name
        self.directory_dictionary = {'/':self.root}
    
    def ls(self):
        self.current_directory.get_children()
    
    def set_path(self):
        self.path = self.current_directory.get_parent() + self.current_directory.get_name() + '/'
    def up_path(self):
        self.path = self.current_directory.get_parent()
    def get_path(self):
        return self.path
        
    def cd(self, dir):
        if dir == '/':
            self.current_directory = self.root
        elif dir == '..':
            self.current_directory = self.current_directory.get_parent()
        else:
            self.current_directory = 

for line in f.readlines():
    if line[0] == "$":
        if line[2:4] == "cd":
            tree.cd(line[5:])
        elif line[2:4] == "ls":
            tree.ls()
    else:
        if line[:3] == 'dir':
            tree.current_directory.add_child(Directory(line[4:]))
        else:
            tree.current_directory.add_child(File(line.split(' ')[1], int(line.split(' ')[0]))
    
$ cd /
$ ls
dir dpbwg
dir dvwfscw
dir hccpl
dir jsgbg
dir lhjmzsl
63532 mwvbpw.mmg
239480 npj
dir pngs
dir qhs
303649 shvgmwn.vhv
236905 sjrrgd.phh
dir sntcp
dir sqs
$ cd dpbwg
$ ls
dir dgh
100731 dpbwg
dir rpwnv
$ cd dgh
"""