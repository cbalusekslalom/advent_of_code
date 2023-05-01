"""
Repo structure
How to build a tree in python
"""
import json


class Tree:
    # use a dictionary to track items by name and values are Directory/File objects
    # pwd is a current state pointer
    def __init__(self):
        self.dictionary = {}
        self.root = '/' # the starting directory
        self.path = self.root    # pwd is the dictionary key
        self.dictionary[self.root] = Directory('/') # dictionary value holds the directory objects

    def ls(self):
        print(json.dumps(self.dictionary[self.path].print_directory(), indent=4))

    def pwd(self):
        return self.path

    def append_path(self,objName):
        if self.path == self.root:
            return self.path + objName
        else:
            return self.path + '/' + objName

    def mkdir(self, dir):
        if dir not in self.dictionary[self.path]:
            self.dictionary[self.append_path(dir)] = Directory(dir)
            self.dictionary[self.append_path(dir)].set_parent(self.path)
        else:
            print(f"Directory {dir} already exists.")

    def touch(self, filename, size):
        if filename not in self.dictionary[self.path].get_children():
            self.dictionary[self.append_path(filename)] = File(filename, size)

    def cd(self, directory):
        if directory in self.dictionary[self.dictionary[directory].get_parent()].get_children():
            self.path = self.dictionary[directory]
        elif directory == '..':
            self.path = self.dictionary[directory.get_parent()]
        elif directory == '/':
            self.path = self.dictionary[self.root]
        else:
            print("Directory Does Not Exist")


class Directory:
    def __init__(self, name, children=[], parent=''):
        self.name = name
        self.children = children
        self.size = 0
        self.parent = parent
    def get_name(self):
        return self.name
    def add_child(self, child):
        self.children.append(child)
    def get_children(self):
        if not self.children:
            return {}
        return [child.get_desc() for child in self.children]
    def print_directory(self):
        print(f"{self.name} -> {self.size}.")
        for child in self.children:
            if type(child) == Directory:
                child.print_directory()
            elif type(child) == File:
                child.print_file()
            else:
                print("invalid data type")
    def set_size(self):
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
        assert isinstance(Directory)
        if self.name == '/':
            self.parent = None
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
        print(f"{self.name} -> {self.size}.")
    def set_name(self, name: str):
        self.name = name
    def get_name(self):
        return self.name
    def set_size(self, size: int):
        self.size = size
    def get_size(self):
        return self.size
    def set_parent(self, parent):
        assert isinstance(Directory)
        self.parent = parent
    def get_parent(self):
        return self.parent

def main():
    dirTree = Tree()
    with open('input.txt') as f:
        for line in f.readlines():
            line_list = line.split(' ')
            if line_list[0] == '$':
                if line_list[1] == 'ls':
                    dirTree.ls()
                elif line_list[1] == 'cd':
                    dirTree.cd(line_list[2])
            elif line_list[0] == 'dir':
                dirTree.mkdir(line_list[1])
            else:
                dirTree.touch(line_list[1], int(line_list[0]))
    dirTree.ls()

if __name__ == "__main__":
    main()