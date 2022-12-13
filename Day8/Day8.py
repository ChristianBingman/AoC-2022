#!//usr/bin/env python3

from sys import argv
from enum import Enum
#from queue import Queue

#class Tree:
#    def __init__(self, height: int):
#        self.height = height
#        self.visible = False
#        self.tallestLeft = None
#        self.tallestRight = None
#        self.tallestAbove = None
#        self.tallestBelow = None
#        self.visitedAbove = False
#        self.visitedBelow = False
#        self.visitedRight = False
#        self.visitedLeft = False
#
#    def setvisible(self, isvisible: bool):
#        self.visible = isvisible
#    def setTallestLeft(self, tallest: int):
#        self.tallestLeft = tallest
#    def setTallestRight(self, tallest: int):
#        self.tallestRight = tallest
#    def setTallestAbove(self, tallest: int):
#        self.tallestAbove = tallest
#    def setTallestBelow(self, tallest: int):
#        self.tallestBelow = tallest
#
#def part1(forest):
#    # BFS from top left
#    q = []
#    q.append([0,0])
#    forest[0][0].visitedAbove = True
#    forest[0][0].visitedLeft = True
#    while len(q) != 0:
#        current = q.pop(0)
#        curtree = forest[current[0]][current[1]]
#        if (current[0] == 0):
#            curtree.setTallestAbove(0)
#        else:
#            curtree.setTallestAbove(max(forest[current[0]-1][current[1]].height, forest[current[0]-1][current[1]].tallestAbove))
#        if (current[1] == 0):
#            curtree.setTallestLeft(0)
#        else:
#            curtree.setTallestLeft(max(forest[current[0]][current[1]-1].height, forest[current[0]][current[1]-1].tallestLeft))
#
#        if current[0]+1 < len(forest) and forest[current[0]+1][current[1]].visitedAbove == False:
#            forest[current[0]+1][current[1]].visitedAbove = True
#            q.append([current[0]+1, current[1]])
#        if current[1]+1 < len(forest[0]) and forest[current[0]][current[1]+1].visitedLeft == False:
#            forest[current[0]][current[1]+1].visitedLeft = True
#            q.append([current[0], current[1]+1])
#    # BFS from bottom right
#    q.append([len(forest)-1,len(forest[0])-1])
#    forest[len(forest)-1][len(forest[0])-1].visitedBelow = True
#    forest[len(forest)-1][len(forest[0])-1].visitedRight = True
#    while len(q) != 0:
#        current = q.pop(0)
#        curtree = forest[current[0]][current[1]]
#        if (current[0] == len(forest)-1):
#            curtree.setTallestBelow(0)
#        else:
#            curtree.setTallestBelow(max(forest[current[0]+1][current[1]].height, forest[current[0]+1][current[1]].tallestBelow))
#        if (current[1] == len(forest[0])-1):
#            curtree.setTallestRight(0)
#        else:
#            curtree.setTallestRight(max(forest[current[0]][current[1]+1].height, forest[current[0]][current[1]+1].tallestRight))
#
#        if current[0]-1 >= 0 and forest[current[0]-1][current[1]].visitedBelow == False:
#            forest[current[0]-1][current[1]].visitedBelow = True
#            q.append([current[0]-1, current[1]])
#        if current[1]-1 >= 0 and forest[current[0]][current[1]-1].visitedRight == False:
#            forest[current[0]][current[1]-1].visitedRight = True
#            q.append([current[0], current[1]-1])
#    # Traverse to set and count visible nodes
#    totalvisibletrees = 0
#    for row in range(len(forest)):
#        for tree in range(len(forest[row])):
#            if (row == 0 or row == len(forest)-1 or tree == 0 or tree == len(forest[0]) or forest[row][tree].height > min(forest[row][tree].tallestAbove, forest[row][tree].tallestBelow, forest[row][tree].tallestLeft, forest[row][tree].tallestRight)):
#                totalvisibletrees += 1
#
#    return totalvisibletrees

class Direction(Enum):
    NORTH = 1
    WEST = 2
    SOUTH = 3
    EAST = 4

def isvisibledirection(dir: Direction, forest, tree) -> bool:
    tree_row = tree[0]
    tree_column = tree[1]
    tree_height = forest[tree_row][tree_column]
    maxtree = 0
    if dir == Direction.NORTH:
        while tree_row != 0:
            tree_row -= 1
            current_tree = forest[tree_row][tree_column]
            if (current_tree >= tree_height):
                return False
            maxtree = max(maxtree, current_tree)
    elif dir == Direction.WEST:
        while tree_column != 0:
            tree_column -= 1
            current_tree = forest[tree_row][tree_column]
            if (current_tree >= tree_height):
                return False
            maxtree = max(maxtree, current_tree)
    elif dir == Direction.SOUTH:
        while tree_row != len(forest)-1:
            tree_row += 1
            current_tree = forest[tree_row][tree_column]
            if (current_tree >= tree_height):
                return False
            maxtree = max(maxtree, current_tree)
    elif dir == Direction.EAST:
        while tree_column != len(forest[0])-1:
            tree_column += 1
            current_tree = forest[tree_row][tree_column]
            if (current_tree >= tree_height):
                return False
            maxtree = max(maxtree, current_tree)
    return True

def part1(forest):
    numvisible = 0
    for tree_row in range(len(forest)):
        for tree_column in range(len(forest[0])):
            if tree_row == 0 or tree_row == len(forest)-1 or tree_column == 0 or tree_column == len(forest[0])-1:
                numvisible += 1
                continue
            current_tree = [tree_row, tree_column]
            if isvisibledirection(Direction.NORTH, forest, current_tree) or isvisibledirection(Direction.WEST, forest, current_tree) or isvisibledirection(Direction.SOUTH, forest, current_tree) or isvisibledirection(Direction.EAST, forest, current_tree):
                numvisible += 1
    return numvisible

def numvisibledirection(dir: Direction, forest, tree) -> int:
    tree_row = tree[0]
    tree_column = tree[1]
    tree_height = forest[tree_row][tree_column]
    numtrees = 0
    if dir == Direction.NORTH:
        while tree_row != 0:
            tree_row -= 1
            current_tree = forest[tree_row][tree_column]
            if (current_tree >= tree_height):
                return numtrees + 1
            numtrees = numtrees + 1
    elif dir == Direction.WEST:
        while tree_column != 0:
            tree_column -= 1
            current_tree = forest[tree_row][tree_column]
            if (current_tree >= tree_height):
                return numtrees + 1
            numtrees = numtrees + 1
    elif dir == Direction.SOUTH:
        while tree_row != len(forest)-1:
            tree_row += 1
            current_tree = forest[tree_row][tree_column]
            if (current_tree >= tree_height):
                return numtrees + 1
            numtrees = numtrees + 1
    elif dir == Direction.EAST:
        while tree_column != len(forest[0])-1:
            tree_column += 1
            current_tree = forest[tree_row][tree_column]
            if (current_tree >= tree_height):
                return numtrees + 1
            numtrees = numtrees + 1
    return numtrees or 1

def part2(forest):
    #TODO: Implement this
    maxscore = 1
    for tree_row in range(len(forest)):
        for tree_column in range(len(forest[0])):
            current_tree = [tree_row, tree_column]
            current_score = 1
            current_score *= numvisibledirection(Direction.EAST, forest, current_tree)
            current_score *= numvisibledirection(Direction.WEST, forest, current_tree)
            current_score *= numvisibledirection(Direction.SOUTH, forest, current_tree)
            current_score *= numvisibledirection(Direction.NORTH, forest, current_tree)
            maxscore = max(maxscore, current_score)
    return maxscore


def main() -> None:
    if len(argv) < 2:
        print(f"Invalid input\nUsage: {argv[0]} <inputfile>\n")
        exit(1)
    lines = open(argv[1]).readlines()
    forest = []
    for line in range(len(lines)):
        forest.append([])
        for tree in lines[line].strip():
            forest[line].append(int(tree))

    print(f"Part 1 Solution: {part1(forest)}")
    print(f"Part 2 Solution: {part2(forest)}")

if __name__ == "__main__":
    main()
