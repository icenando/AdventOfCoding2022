def part_1():
    with (open("4/input.txt") as f):
        overlapsFullyTotal = 0
        lines = f.readlines()
        for line in lines:
            areas = line.split(",")
            elf_1, elf_2 = areas[0].split("-"), areas[1].replace("\n", "").split("-")
            elf_1, elf_2 = [int(area) for area in elf_1], [int(area) for area in elf_2]
            if (min(elf_1) >= min(elf_2) and max(elf_1) <= max(elf_2)) or (
                min(elf_2) >= min(elf_1) and max(elf_2) <= max(elf_1)
            ):
                overlapsFullyTotal += 1

    print(overlapsFullyTotal)


def part_2():
    return


part_1()
part_2()
