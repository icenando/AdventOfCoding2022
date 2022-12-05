import re


# SETUP
with(open("5/input.txt") as f):
    initial = f.readlines()

rows_of_boxes, stack_nums = initial[0:8], initial[8].split()
for i, row in enumerate(rows_of_boxes):
    # WARNING! ***** NSFW *****
    rows_of_boxes[i] = rows_of_boxes[i][:-1].replace("    ", "[]").replace(" ", "").replace("][", "] [").split()

instructions = initial[10::]
for i, line in enumerate(instructions):
    instructions[i] = list(map(int, re.findall(r'\d+', instructions[i])))

stacks_dict = {key: list() for key in stack_nums}
for stack in stack_nums:
    for row in rows_of_boxes:
        box = row[int(stack)-1]
        if box != "[]":
            stacks_dict[stack].append(row[int(stack)-1])
    stacks_dict[stack].reverse()

# for i in stack_nums:
#     print(stacks_dict[i])

# def move_crates_1(quantity, origin, destination):
#     global stacks_dict
#     for i in range(quantity):
#         crate = stacks_dict[str(origin)].pop()
#         stacks_dict[str(destination)].append(crate)

def move_creates_2(quantity, origin, destination):
    global stacks_dict
    crates_to_move = len(stacks_dict[str(origin)]) - quantity
    crates = stacks_dict[str(origin)][crates_to_move::]
    del stacks_dict[str(origin)][crates_to_move::]
    stacks_dict[str(destination)].extend(crates)

for instruction in instructions:
    # move_crates_1(instruction[0], instruction[1], instruction[2])
    move_creates_2(instruction[0], instruction[1], instruction[2])

for i in stack_nums:
    print(stacks_dict[i][-1])