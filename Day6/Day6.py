#!//usr/bin/env python3

from sys import argv
from copy import deepcopy

def findnodupsub(line, num) -> int:
    for ind in range(num,len(line)):
        subs = line[ind-num:ind]
        if len(subs) == len(set(subs)):
            return ind

def part1(line) -> int:
    #TODO: Implement this
    return findnodupsub(line, 4)

def part2(line) -> int:
    #TODO: Implement this
    return findnodupsub(line, 14)

def main() -> None:
    if len(argv) < 2:
        print(f"Invalid input\nUsage: {argv[0]} <inputfile>\n")
        exit(1)
    lines = open(argv[1]).readlines()
    print(f"Part 1 Solution: {part1(deepcopy(lines)[0])}")
    print(f"Part 2 Solution: {part2(deepcopy(lines)[0])}")

if __name__ == "__main__":
    main()
