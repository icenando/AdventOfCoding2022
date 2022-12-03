import string

letters = [letter for letter in string.ascii_letters]

priorityDict = {}
for i in range(len(letters)):
    priorityDict[letters[i]] = i + 1

total = 0

with (open("3/input.txt") as f):
    for bag in f.readlines():
        bagSize = len(bag)
        compartment_1 = bag[0 : bagSize // 2]
        compartment_2 = bag[bagSize // 2 : -1]

        found_items = []

        for item in compartment_1:
            if item in compartment_2 and item not in found_items:
                found_items.append(item)
                total += priorityDict[item]

print(total)
