#!//usr/bin/env python3

from sys import argv
from copy import deepcopy
from functools import cmp_to_key

def check_packet(left: list[int], right: list[int]) -> int:
    # Store the size of the right list for easy access
    right_size = len(right)
    # For each pair on left and right
    for idx in range(len(left)):
        # If the index >= the size of the right
        if idx >= right_size:
            return -1
        # If both sides are equal
        if left[idx] == right[idx]:
            continue
        # Check if either the left is int and right is array, and vice versa
        if type(left[idx]) == list and type(right[idx]) == int:
            # Convert the type of the int to array
            right_arr = [right[idx]]
            # Check if arrays are equal
            if left[idx] == right_arr:
                # Continue to next pair
                continue
            # If not
            else:
                # Continue recursive calls on the arrays
                return check_packet(left[idx], right_arr)
        if type(left[idx]) == int and type(right[idx]) == list:
            # Convert the type of the int to array
            left_arr = [left[idx]]
            # Check if arrays are equal
            if left_arr == right[idx]:
                # Continue to next pair
                continue
            # If not
            else:
                # Continue recursive calls on the arrays
                return check_packet(left_arr, right[idx])
        # If both sides are arrays
        if type(left[idx]) == list and type(right[idx]) == list:
            # Recurse into both sides
            return check_packet(left[idx], right[idx])
        # If left < right
        if left[idx] < right[idx]:
            return 1
        # If left > right
        if left[idx] > right[idx]:
            return -1
    # Default case where the entire array is equal, or the size of the left array is shorter than the right, return true
    return 0

def part1(lines: list[str]) -> int:
    # Call recursive packet check
    total_correct = 0
    # For every two lines
    for linenum in range(0, len(lines), 3):
        # Check each set of packets and increase it by the index of the packets for each success, otherwise don't add anything
        total_correct += int((linenum/3)+1) if check_packet(eval(lines[linenum]), eval(lines[linenum+1])) >= 0 else 0
    return total_correct
    
def part2(lines: list[str]):
    # Remove all empty lines from lines, eval them, add [[2]] and [[6]] to the list, and sort them
    sorted_packets = sorted([eval(line) for line in list(filter(lambda x: x != "", lines))] + [[[2]], [[6]]], key=cmp_to_key(check_packet), reverse=True)
    print('\n'.join([str(packet) for packet in sorted_packets]))
    decoder_key = 1
    for packet in range(len(sorted_packets)):
        if sorted_packets[packet] == [[2]] or sorted_packets[packet] == [[6]]:
            decoder_key *= packet+1
    return decoder_key

def main() -> None:
    if len(argv) < 2:
        print(f"Invalid input\nUsage: {argv[0]} <inputfile>\n")
        exit(1)
    lines = open(argv[1]).read().splitlines()

    print(f"Part 1 Solution: {part1(deepcopy(lines))}")
    print(f"Part 2 Solution: {part2(deepcopy(lines))}")

if __name__ == "__main__":
    main()
