#!//usr/bin/env python3

from sys import argv
from enum import Enum
import math
from itertools import groupby
from copy import copy

class Direction(Enum):
    RIGHT = 'R'
    UP = 'U'
    DOWN = 'D'
    LEFT = 'L'


def part1(lines):
    # Track the current head of the rope
    head = [0,0]
    # Track the previous position of the head of the rope
    prev_head = [0,0]
    # Track the tail of the rope
    tail = [0,0]
    # Track the positions the tail has been
    positions = [(0,0)]
    # For each requested direction
    for line in lines:
        line = line.strip().split(' ')
        direction = Direction(line[0])
        distance = int(line[1])
        while distance != 0:
            # Move head in the direction
            prev_head = [head[0], head[1]]
            if direction == Direction.UP:
                head = [head[0],head[1]+1]
            elif direction == Direction.DOWN:
                head = [head[0],head[1]-1]
            elif direction == Direction.LEFT:
                head = [head[0]-1,head[1]]
            elif direction == Direction.RIGHT:
                head = [head[0]+1,head[1]]
            # Check the distance between the head and tail
            htdist = math.sqrt((head[0]-tail[0])**2 + (head[1]-tail[1])**2)
            # If the distance is larger than 1.5 
            if htdist > 1.5:
                # Move the tail to the previous position the head was in
                tail = [prev_head[0], prev_head[1]]
                # Add the tail location to the list of positions
                positions.append((tail[0], tail[1]))
            distance -= 1
    # Convert the list of positions the tail has been in to a set
    # Return the size of the set
    return len(set(positions))


def part2(lines):
    # Create a rope with 10 knots
    rope = [(0,0)]*10
    # Create a list of tail positions
    positions = [(0,0)]
    # For each requested direction
    for line in lines:
        line = line.strip().split(' ')
        direction = Direction(line[0])
        distance = int(line[1])
        # For each time the head needs to move in that direction
        while distance != 0:
            # Update the head
            if direction == Direction.UP:
                rope[0] = (rope[0][0],rope[0][1]+1)
            elif direction == Direction.DOWN:
                rope[0] = (rope[0][0],rope[0][1]-1)
            elif direction == Direction.LEFT:
                rope[0] = (rope[0][0]-1,rope[0][1])
            elif direction == Direction.RIGHT:
                rope[0] = (rope[0][0]+1,rope[0][1])
            # For each knot
            for knot in range(len(rope)-1):
                # Check the distance between the current and the next
                htdist = math.sqrt((rope[knot][0]-rope[knot+1][0])**2 + (rope[knot][1]-rope[knot+1][1])**2)
                # If the distance is > 1.5
                if htdist > 1.5:
                    # Normalize the distance to the next knot (x, x)
                    normalized = (rope[knot][0] - rope[knot+1][0], rope[knot][1] - rope[knot+1][1])
                    # Halve the distance (x/2, x/2)
                    # ceil each side (roof(x/2), roof(x/2))
                    tomove = (math.copysign(math.ceil(abs(normalized[0]/2)), normalized[0]), math.copysign(math.ceil(abs(normalized[1]/2)), normalized[1]))
                    # Add the change to the current knot
                    rope[knot+1] = (rope[knot+1][0] + tomove[0], rope[knot+1][1] + tomove[1])
            # Add the tail to the current list of positions
            positions.append(rope[-1])
            distance -= 1
    # Convert the list of positions the tail has been in to a set
    # Return the size of the set
    return len(set(positions))


def main() -> None:
    if len(argv) < 2:
        print(f"Invalid input\nUsage: {argv[0]} <inputfile>\n")
        exit(1)
    lines = open(argv[1]).readlines()

    print(f"Part 1 Solution: {part1(lines)}")
    print(f"Part 2 Solution: {part2(lines)}")

if __name__ == "__main__":
    main()
