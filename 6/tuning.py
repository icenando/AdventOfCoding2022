def part_1(signals):
    current_signal = []

    for pointer_start in range(len(signals)):
        current_signal.append(signals[pointer_start])
        for pointer_end in range(1, 4):
            if signals[pointer_start] != signals[pointer_end]:
                current_signal.append(signals[pointer_end])
                if len(current_signal) == 4:
                    return pointer_end + 1
            else:
                current_signal = [current_signal[pointer_start + 1]]
                pointer_start += pointer_end

    return


if __name__ == "__main__":
    with (open("6/input.txt") as f):
        signals = f.read()
    part_1(signals)
