#!/usr/bin/env python3

from sys import argv

def priority(char: str) -> int:
    if char.islower():
        return ord(char)-96
    elif char.isupper():
        return ord(char)-38
    return 0


def part1(lines):
    # Rucksack contains an even number of items
    totalpriorities = 0
    for line in lines:
        line = line.strip()
        # Split the rucksack into 2 parts
        compartment1 = line[:int(len(line)/2)]
        compartment2 = line[int(len(line)/2):]
        letters = [0]*52
        # For every character found, add it to a count for the first half
        for char in compartment1:
            if char.islower():
                letters[ord(char)-71] += 1
            else:
                letters[ord(char)-65] += 1
        # Find the first letter that we have from the first half
        for char in compartment2:
            if char.islower() and letters[ord(char)-71] != 0:
                totalpriorities += priority(char)
                break
            elif char.isupper() and letters[ord(char)-65] != 0:
                totalpriorities += priority(char)
                break
    print(totalpriorities)


def part2(lines):
    print("Do part 2")
    totalpriorities = 0
    for elfset in range(int(len(lines)/3)):
        # Deduplicate the lines
        elf1 = list(set(lines[3*elfset].strip())) 
        elf2 = list(set(lines[(3*elfset)+1].strip())) 
        elf3 = list(set(lines[(3*elfset)+2].strip())) 
        # Concatenate the lines
        combined = elf1 + elf2 + elf3
        # Sort the lines
        combined.sort()
        # Find the first repetition of 3 elements
        currentlettercount = 0
        currentletter = combined[0]
        for letter in combined:
            if(currentletter == letter):
                currentlettercount += 1
                if currentlettercount == 3:
                    totalpriorities += priority(currentletter)
                    break
            else:
                currentletter = letter
                currentlettercount = 1
    print(totalpriorities)

def main():
    if len(argv) < 2:
        print(f"Invalid input\nUsage: {argv[0]} <inputfile>\n")
        exit(1)
    lines = open(argv[1]).readlines()
    part1(lines)
    part2(lines)

if __name__ == "__main__":
    main()
