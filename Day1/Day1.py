#!/usr/bin/env python3
from queue import PriorityQueue

max = 0
curtotal = 0
with open('input.txt') as file:
    for calories in file.readlines():
        if (calories == "\n"):
            if (curtotal > max):
                max = curtotal
            curtotal = 0
        else:
            curtotal += int(calories)


print(f"One elf max: {max}")


# Hold 3 elfs
elves = [0, 0, 0]
currentminmax = 0
currentminmaxelem = 0
# current total
curtotal = 0

with open('input.txt') as file:
    # for each line in file
    for calories in file.readlines():
        # count the total calories for that elf
        if (calories == "\n"):
            # if that elf is carrying more than the lowest total elf
            if (curtotal > currentminmax):
                # replace the total for the lowest elf with the current total
                elves[currentminmaxelem] = curtotal
                currentminmax = curtotal

                for elf in range(3):
                    if (elves[elf] < currentminmax):
                        currentminmax = elves[elf]
                        currentminmaxelem = elf
            # reset the current total
            curtotal = 0
        else:
            curtotal += int(calories)
                    
print(elves)

# More clear solution

q = PriorityQueue()

with open('input.txt') as file:
    for calories in file.readlines():
        if (calories == "\n"):
            q.put(-curtotal)
            curtotal = 0
        else:
            curtotal += int(calories)

print(-(q.get()+q.get()+q.get()))
