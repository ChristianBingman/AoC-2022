#!//usr/bin/env python3

from sys import argv
from enum import Enum
from copy import deepcopy
from math import floor,inf
from functools import reduce
from operator import mul

class Monkey:
    def __init__(self, starting_items: list[int], operation, test: int, truemonkey: int, falsemonkey: int):
        self.starting_items = starting_items
        self.operation = operation
        self.test = test
        self.truemonkey = truemonkey
        self.falsemonkey = falsemonkey
        self.num_inspects = 0
    
    def inspect_items(self, divide_by_three: bool = True, lcm = inf) -> list[tuple[int]]:
        thrown_items = []
        monkey_to = -1
        for item in self.starting_items:
            item = item % lcm
            self.num_inspects += 1
            item = floor(self.operation(item) / 3) if divide_by_three else floor(self.operation(item))
            if ((item % self.test) == 0):
                monkey_to = self.truemonkey
            else:
                monkey_to = self.falsemonkey
            thrown_items.append((item, monkey_to))
        self.starting_items.clear()
        return thrown_items

    def add_item(self, value: int):
        self.starting_items.append(value)

def part1(monkeys: list[Monkey]) -> int:
    num_rounds = 20
    # For every round
    for _ in range(num_rounds):
        # For every monkey
        for monkey in monkeys:
            # Have monkey inspect all items and return the worry levels and to monkeys
            to_update = monkey.inspect_items()
            # Add item to each monkeys inventory
            for key, val in to_update:
                monkeys[val].add_item(key)
    # Find the max 2 monkeys that have touched items
    sort_monkeys = sorted([x.num_inspects for x in monkeys])
    # Return the 2 monkeys multiplied together
    return sort_monkeys[-1] * sort_monkeys[-2]

def part2(monkeys: list[Monkey]):
    # If we mod every item by a number that is larger than what we would mod by in our test
    # then the mod in the test will result in the same answer
    # We need to find the LCM
    lcm = reduce(mul, [x.test for x in monkeys])
    num_rounds = 10000
    # For every round
    for _ in range(num_rounds):
        # For every monkey
        for monkey in monkeys:
            # Have monkey inspect all items and return the worry levels and to monkeys
            # Also pass in our lcm to mod all of the items by
            to_update = monkey.inspect_items(lcm=lcm, divide_by_three=False)
            # Add item to each monkeys inventory
            for key, val in to_update:
                monkeys[val].add_item(key)
    # Find the max 2 monkeys that have touched items
    sort_monkeys = sorted([x.num_inspects for x in monkeys])
    # Return the 2 monkeys multiplied together
    return sort_monkeys[-1] * sort_monkeys[-2]

def get_operation_fn(operation_str: list[str]):
    if operation_str[1] == "*":
        if operation_str[2] == "old":
            return lambda x: x*x
        else:
            operand = int(operation_str[2])
            return lambda x: x*operand
    else:
        if operation_str[2] == "old":
            return lambda x: x+x
        else:
            operand = int(operation_str[2])
            return lambda x: x+operand

def main() -> None:
    if len(argv) < 2:
        print(f"Invalid input\nUsage: {argv[0]} <inputfile>\n")
        exit(1)
    lines = open(argv[1]).readlines()
    lines = list(filter(lambda x: x != "\n", lines))
    monkeys = []
    chunk_size = 6
    for monkey in range(0, len(lines), chunk_size):
        starting_items = [int(x) for x in lines[monkey+1].strip().split(':')[1].split(',')]
        operation = get_operation_fn(lines[monkey+2].split('=')[1].strip().split(' '))
        test = int(lines[monkey+3].split(' ')[-1])
        truemonkey = int(lines[monkey+4].split(' ')[-1])
        falsemonkey = int(lines[monkey+5].split(' ')[-1])
        monkeys.append(Monkey(starting_items, operation, test, truemonkey, falsemonkey))
    
    print(f"Part 1 Solution: {part1(deepcopy(monkeys))}")
    print(f"Part 2 Solution: {part2(deepcopy(monkeys))}")

if __name__ == "__main__":
    main()
