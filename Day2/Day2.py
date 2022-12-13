#!/usr/bin/env python3

from enum import Enum

lines = open('./input.txt').readlines()

class ShapeUs(Enum):
    ROCK = "X"
    PAPER = "Y"
    SCISSORS = "Z"

class ShapeOpponent(Enum):
    ROCK = 'A'
    PAPER = 'B'
    SCISSORS = 'C'

def match(opponent: ShapeOpponent, us: ShapeUs) -> int:
    # Tie
    if (opponent.name == us.name):
        return 3
    elif (opponent == ShapeOpponent.ROCK and us == ShapeUs.PAPER):
        return 6
    elif (opponent == ShapeOpponent.PAPER and us == ShapeUs.SCISSORS):
        return 6
    elif (opponent == ShapeOpponent.SCISSORS and us == ShapeUs.ROCK):
        return 6
    return 0

def main():
    totalscore = 0
    # For each item in lines
    for line in lines:
        line = line.strip()
        opponent = line.split()[0]
        us = line.split()[1]
        # Add choice to total rock (1), paper (2), scissors (3) and add to total
        if (ShapeUs(us) == ShapeUs.ROCK):
            totalscore += 1
        if (ShapeUs(us) == ShapeUs.PAPER):
            totalscore += 2
        if (ShapeUs(us) == ShapeUs.SCISSORS):
            totalscore += 3
        # Check if we won (6), lost (0), or draw (3) and add to total
        totalscore += match(ShapeOpponent(opponent), ShapeUs(us))
    print(totalscore)

if __name__ == "__main__":
    main()

