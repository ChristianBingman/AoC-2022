#!/usr/bin/env python3

from enum import Enum

lines = open('./input.txt').readlines()

class MatchResult(Enum):
    LOSE = "X"
    DRAW = "Y"
    WIN = "Z"

class ShapeOpponent(Enum):
    ROCK = 'A'
    PAPER = 'B'
    SCISSORS = 'C'

class ShapeValues(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

def match(opponent: ShapeOpponent, MatchResult: MatchResult) -> int:
    # Tie
    if (MatchResult == MatchResult.DRAW):
        return ShapeValues[opponent.name].value
    elif (MatchResult == MatchResult.WIN):
        if (opponent == ShapeOpponent.ROCK):
            return ShapeValues.PAPER.value
        elif (opponent == ShapeOpponent.PAPER):
            return ShapeValues.SCISSORS.value
        elif (opponent == ShapeOpponent.SCISSORS):
            return ShapeValues.ROCK.value
    elif (MatchResult == MatchResult.LOSE):
        if (opponent == ShapeOpponent.ROCK):
            return ShapeValues.SCISSORS.value
        elif (opponent == ShapeOpponent.PAPER):
            return ShapeValues.ROCK.value
        elif (opponent == ShapeOpponent.SCISSORS):
            return ShapeValues.PAPER.value

def main():
    totalscore = 0
    # For each item in lines
    for line in lines:
        line = line.strip()
        opponent = ShapeOpponent(line.split()[0])
        result = MatchResult(line.split()[1])
        totalscore += match(opponent, result)
        if (result == MatchResult.DRAW):
            totalscore += 3
        elif (result == MatchResult.WIN):
            totalscore += 6
    print(totalscore)

if __name__ == "__main__":
    main()

