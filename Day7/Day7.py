#!//usr/bin/env python3

from sys import argv
from copy import deepcopy
from enum import Enum

class InodeType(Enum):
    FILE = 1
    FOLDER = 2

class Inode:
    root = None
    def __init__(self, name: str, size: float, type: InodeType):
        if (self.root == None):
            self.root = self
        self.children = []
        self.size = 0
        self.name = name
        self.type = type
        self.parent = None

    def add_folder(self, name: str):
        new_node = Inode(name, 0, InodeType.FOLDER)
        new_node.parent = self
        self.children.append(new_node)
        return new_node
    def add_file(self, name: str, size: float):
        self.children.append(Inode(name, size, InodeType.FILE))
        currentnode = self
        while (currentnode.name != '/'):
            currentnode.size += size
            currentnode = currentnode.parent
        currentnode.size += size
    def get_child_by_name(self, name: str):
        for child in self.children:
            if child.name == name:
                return child

def recursecount(currentnode: Inode, untilless: float) -> float:
    total = 0
    for child in currentnode.children:
        if child.type == InodeType.FOLDER:
            total += recursecount(child, untilless)
    if currentnode.size < untilless:
        return currentnode.size + total
    else:
        return total

def freespace(currentnode: Inode, amount: float, currentmin: Inode) -> Inode:
    minnode = currentnode
    for child in currentnode.children:
        if child.type == InodeType.FOLDER and child.size > amount:
            smallest = freespace(child, amount, currentmin)
            if smallest.size < minnode.size:
                minnode = smallest
    return minnode

def part1(filetree: Inode):
    #TODO: Implement this
    return recursecount(filetree, 100000)

def part2(filetree: Inode):
    #TODO: Implement this
    spaceneeded = 30000000 - (70000000 - filetree.size)
    return freespace(filetree, spaceneeded, filetree).size


def main() -> None:
    if len(argv) < 2:
        print(f"Invalid input\nUsage: {argv[0]} <inputfile>\n")
        exit(1)
    lines = open(argv[1]).readlines()
    filetree = Inode("/", 0, InodeType.FOLDER)
    currentnode = filetree
    for line in lines[1:]:
        line = line.strip()
        if (line[0] == '$'):
            if (line[2:4] == "cd"):
                if (line[5:] == ".."):
                    currentnode = currentnode.parent
                else:
                    currentnode = currentnode.get_child_by_name(line[5:])
        else:
            # ls
            if (line[:3] == "dir"):
                currentnode.add_folder(line[4:])
            else:
                # file
                filedata = line.split(' ')
                currentnode.add_file(filedata[1], float(filedata[0]))

    print(f"Part 1 Solution: {part1(filetree)}")
    print(f"Part 2 Solution: {part2(filetree)}")

if __name__ == "__main__":
    main()
