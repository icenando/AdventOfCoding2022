max_cal = 0

with (open("input.txt") as f):
    tempSum = 0
    for elf in f.readlines():
        if elf == "\n":
            max_cal = max(max_cal, tempSum)
            tempSum = 0
        else:
            tempSum += int(elf[:-1])


print(max_cal)
