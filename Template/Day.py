#!//usr/bin/env python3

from sys import argv
from copy import deepcopy

def part1(lines: list[str]):
    pass

def part2(lines: list[str]):
    pass

def main() -> None:
    if len(argv) < 2:
        print(f"Invalid input\nUsage: {argv[0]} <inputfile>\n")
        exit(1)
    lines = open(argv[1]).read().splitlines()

    print(f"Part 1 Solution: {part1(deepcopy(lines))}")
    print(f"Part 2 Solution: {part2(deepcopy(lines))}")

if __name__ == "__main__":
    main()
