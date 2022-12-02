max_cal = [0, 0, 0]

with (open("1/input.txt") as f):
    tempSum = 0
    for elf in f.readlines():
        if elf == "\n":
            for i in range(3):
                if tempSum > max_cal[i]:
                    max_cal[i], tempSum = tempSum, max_cal[i]
            tempSum = 0
        else:
            tempSum += int(elf[:-1])

print(sum(max_cal))

# 199172
