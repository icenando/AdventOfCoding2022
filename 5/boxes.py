with(open("5/input.txt") as f):
    initial = f.readlines()

rows_of_boxes, stack_nums = initial[0:8], initial[8].split()
for i, row in enumerate(rows_of_boxes):
    # WARNING! ***** NSFW *****
    rows_of_boxes[i] = rows_of_boxes[i][:-1].replace("    ", "[]").replace(" ", "").replace("][", "] [").split()

instructions = initial[9::]
# stacks_dict = dict.fromkeys(stack_nums, [])
stacks_dict = {key: list() for key in stack_nums}

for stack in stack_nums:
    for row in rows_of_boxes:
        box = row[int(stack)-1]
        if box != "[]":
            stacks_dict[stack].append(row[int(stack)-1])

print(stacks_dict)