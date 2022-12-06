def part_1(signals):
    current_len = []
    for i in range(len(signals)-4):
        current_len.append(signals[i])
        for j in range(1, 4):
            # print(signals[i], signals[i+j])
            if signals[i+j] in current_len:
                current_len.clear()
                break
            else:
                current_len.append(signals[i+j])
                if len(current_len) == 4:
                    return i+j+1


if __name__ == "__main__":
    with (open("6/input.txt") as f):
        signals = f.read()
    
    print(part_1(signals))
