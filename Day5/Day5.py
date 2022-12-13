#!//usr/bin/env python3

from sys import argv
from copy import deepcopy

def part1(stacks, lines):
    #TODO: Implement this
    for line in lines:
        line = line.strip().split(' ')
        num = int(line[1])
        fro = int(line[3])-1
        to = int(line[5])-1

        for _ in range(num):
            stacks[to].append(stacks[fro].pop())
    return ''.join([stack.pop() for stack in stacks])

def part2(stacks, lines):
    #TODO: Implement this
    for line in lines:
        line = line.strip().split(' ')
        num = int(line[1])
        fro = int(line[3])-1
        to = int(line[5])-1

        toadd = []
        for _ in range(num):
            toadd.append(stacks[fro].pop())

        stacks[to] = stacks[to] + toadd[::-1]
    return ''.join([stack.pop() for stack in stacks])

def main() -> None:
    if len(argv) < 2:
        print(f"Invalid input\nUsage: {argv[0]} <inputfile>\n")
        exit(1)
    lines = open(argv[1]).readlines()
    numstacks = 0
    height = 0
    for linenum in range(len(lines)):
        if (lines[linenum][1] == '1'):
            numstacks = int(lines[linenum][-3])
            height = linenum
            break
    stacks = [[] for _ in range(numstacks)]

    # Load first stack
    for stack in range(numstacks):
        offset = 1 + (4*stack)
        for crate in reversed(range(height)):
            if (lines[crate][offset] == ' '):
                continue
            stacks[stack].append(lines[crate][offset])

    print(f"Part 1 Solution: {part1(deepcopy(stacks), lines[height+2:])}")
    print(f"Part 2 Solution: {part2(stacks, lines[height+2:])}")

if __name__ == "__main__":
    main()
