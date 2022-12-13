#!//usr/bin/env python3

from sys import argv

def part1(lines):
    #TODO: Implement this
    totaloverlaps = 0
    for line in lines:
        line = line.strip()
        firstsection, secondsection = line.split(',')
        firstsection = firstsection.split('-')
        firstsection = [int(x) for x in firstsection]
        secondsection = secondsection.split('-')
        secondsection = [int(x) for x in secondsection]
        if(firstsection[0] >= secondsection[0] and firstsection[1] <= secondsection[1]):
            totaloverlaps+=1
        elif(firstsection[0] <= secondsection[0] and firstsection[1] >= secondsection[1]):
            totaloverlaps+=1
    print(f"Total complete overlaps: {totaloverlaps}")

def part2(lines):
    #TODO: Implement this
    totaloverlaps = 0
    for line in lines:
        line = line.strip()
        firstsection, secondsection = line.split(',')
        firstsection = firstsection.split('-')
        firstsection = [int(x) for x in firstsection]
        secondsection = secondsection.split('-')
        secondsection = [int(x) for x in secondsection]
        if(firstsection[0] >= secondsection[0] and firstsection[0] <= secondsection[1]):
            totaloverlaps+=1
        elif(firstsection[1] >= secondsection[0] and firstsection[1] <= secondsection[1]):
            totaloverlaps+=1
        elif(secondsection[0] >= firstsection[0] and secondsection[0] <= firstsection[1]):
            totaloverlaps+=1
        elif(secondsection[1] >= firstsection[0] and secondsection[1] <= firstsection[1]):
            totaloverlaps+=1
    print(f"Total overlaps: {totaloverlaps}")

def main() -> None:
    if len(argv) < 2:
        print(f"Invalid input\nUsage: {argv[0]} <inputfile>\n")
        exit(1)
    lines = open(argv[1]).readlines()
    part1(lines)
    part2(lines)

if __name__ == "__main__":
    main()
