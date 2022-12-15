#!//usr/bin/env python3

from sys import argv
from copy import deepcopy
from dataclasses import dataclass
from math import inf

@dataclass
class HMNode:
    height: int
    distance: int = inf

class HeightMap:
    def __init__(self, hm: list[list[str]]):
        # Convert heightmap of strings (a-z) to numbers (0-25) for ez comparisons
        self.hm = [[HMNode(ord(h)-97) for h in row] for row in hm]
        for row in range(len(self.hm)):
            for column in range(len(self.hm[row])):
                if self.hm[row][column].height == -14:
                    self.start = (row, column)
                    self.hm[row][column].height = 0
                elif self.hm[row][column].height == -28:
                    self.end = (row, column)
                    self.hm[row][column].height = 25

    def shortest_path(self, starting: tuple[int]) -> int:
        # Find the shortest path and return the distance

        # Rules
        # - You can only step up by 1
        # - You can step down by any number

        sizex = len(self.hm)
        sizey = len(self.hm[0])
        visited = [[False] * sizey for x in range(sizex)]
        # Store the queue of next nodes
        q = []
        q.append(starting)
        # Set distance of start to 0
        x, y = starting
        self.hm[x][y].distance = 0
        # Set start to visited
        visited[x][y] = True
        # while the queue is not empty
        while len(q) != 0:
            # Pop the front of the queue
            x, y = q.pop(0)
            if (x,y) == self.end:
                return self.hm[x][y].distance
            # For all adjacent
            if x-1 >= 0 and self.hm[x-1][y].height - self.hm[x][y].height <= 1:
                # if the node is not visited
                if not visited[x-1][y]:
                    # Update the nodes distance
                    self.hm[x-1][y].distance = self.hm[x][y].distance + 1
                    # Set node to visited
                    visited[x-1][y] = True
                    # Push the node to the queue
                    q.append((x-1, y))
            if x + 1 < sizex and self.hm[x+1][y].height - self.hm[x][y].height <= 1:
                # if the node is not visited
                if not visited[x+1][y]:
                    # Update the nodes distance
                    self.hm[x+1][y].distance = self.hm[x][y].distance + 1
                    # Set node to visited
                    visited[x+1][y] = True
                    # Push the node to the queue
                    q.append((x+1, y))
            if y - 1 >= 0 and self.hm[x][y-1].height - self.hm[x][y].height <= 1:
                # if the node is not visited
                if not visited[x][y-1]:
                    # Update the nodes distance
                    self.hm[x][y-1].distance = self.hm[x][y].distance + 1
                    # Set node to visited
                    visited[x][y-1] = True
                    # Push the node to the queue
                    q.append((x, y-1))
            if y + 1 < sizey and self.hm[x][y+1].height - self.hm[x][y].height <= 1:
                # if the node is not visited
                if not visited[x][y+1]:
                    # Update the nodes distance
                    self.hm[x][y+1].distance = self.hm[x][y].distance + 1
                    # Set node to visited
                    visited[x][y+1] = True
                    # Push the node to the queue
                    q.append((x, y+1))



def part1(hm: HeightMap) -> int:
    return hm.shortest_path(hm.start)

def part2(hm: HeightMap) -> int:
    # Lazy solution
    # Find all points that have height 0
    apoints = []
    for row in range(len(hm.hm)):
        for column in range(len(hm.hm[row])):
            if hm.hm[row][column].height == 0:
                apoints.append((row, column))
    # Find the minimum of the distance to end for all the points
    return min(filter(lambda x: x != None, [hm.shortest_path(x) for x in apoints]))
def main() -> None:
    if len(argv) < 2:
        print(f"Invalid input\nUsage: {argv[0]} <inputfile>\n")
        exit(1)
    lines = open(argv[1]).read().splitlines()
    hm = HeightMap([line for line in lines])
    #print('\n'.join([' '.join([str(x.height) for x in row]) for row in hm.hm]))

    print(f"Part 1 Solution: {part1(deepcopy(hm))}")
    print(f"Part 2 Solution: {part2(deepcopy(hm))}")

if __name__ == "__main__":
    main()
