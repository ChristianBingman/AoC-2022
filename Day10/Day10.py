#!//usr/bin/env python3

from sys import argv
from enum import Enum

def part1(lines):
    # Count the number of cycles total
    cycle = 1
    # Count the number of cycles required for the current instruction
    instruction_cycle = 0
    # Count register x
    x = 1
    # Track signal strength
    signal_strength = 0
    # Track what will be added at the end of the operation
    toadd = 0
    # For every instruction
    for line in lines:
        line = line.strip().split(' ')
        operation = line[0]
        # If instruction is noop
        if operation == "noop":
            # cycles required = 1
            instruction_cycle = 1
            toadd = 0
        # elif instruction is addx
        else:
            # cycles required = 2
            instruction_cycle = 2
            toadd = int(line[1])
        # while the count of cycles required for the instruction is > 0
        while instruction_cycle > 0:
            # if the current cycle is 20 or the cycle - 20 % 40
            if cycle == 20 or ((cycle - 20) % 40) == 0:
                # signal strength += cycle * register x
                signal_strength += cycle * x
            # cycles += 1
            cycle += 1
            # cycles for current instruction -= 1
            instruction_cycle -= 1
        # Add the x if applicable
        x += toadd

    return signal_strength


def part2(lines):
    # Keep the CRT view array
    crt = []
    # Track the current line on the screen
    crtline = -1
    # Count the number of cycles total
    cycle = 1
    # Count the number of cycles required for the current instruction
    instruction_cycle = 0
    # Count register x
    x = 1
    # Track what will be added at the end of the operation
    toadd = 0
    # For every instruction
    for line in lines:
        line = line.strip().split(' ')
        operation = line[0]
        # If instruction is noop
        if operation == "noop":
            # cycles required = 1
            instruction_cycle = 1
            toadd = 0
        # elif instruction is addx
        else:
            # cycles required = 2
            instruction_cycle = 2
            toadd = int(line[1])
        # while the count of cycles required for the instruction is > 0
        while instruction_cycle > 0:
            # If the cycle is the first in the line
            if (cycle - 1) % 40 == 0:
                # Start a new line on the CRT
                crt.append([])
                crtline += 1
            # If the currently being drawn sprite is within +/- 1 of x
            if (cycle % 40)-1 >= (x-1) and (cycle % 40)-1 <= (x+1):
                # Draw a # to the current CRT line
                crt[crtline].append('#')
            # else
            else:
                # Draw a .
                crt[crtline].append('.')
            # cycles += 1
            cycle += 1
            # cycles for current instruction -= 1
            instruction_cycle -= 1
        # Add the x if applicable
        x += toadd

    crt = '\n'.join([''.join(x) for x in crt])
    return f"\n{crt}"


def main() -> None:
    if len(argv) < 2:
        print(f"Invalid input\nUsage: {argv[0]} <inputfile>\n")
        exit(1)
    lines = open(argv[1]).readlines()

    print(f"Part 1 Solution: {part1(lines)}")
    print(f"Part 2 Solution: {part2(lines)}")

if __name__ == "__main__":
    main()
