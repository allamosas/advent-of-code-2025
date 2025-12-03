from pathlib import Path

def part1(data):
    joltage = calc_joltage(data, 2)       
    return joltage

def part2(data):
    joltage = calc_joltage(data, 12)       
    return joltage

def calc_joltage(data, digits):
    joltage = 0
    for line in data:
        line = list(line)
        largest_num_pos = max(range(len(line)-digits+1), key=lambda i: int(line[i]))
        sliced_line = line[largest_num_pos:]
        while len(sliced_line) > digits:
            for pos in range(len(sliced_line) - 1):
                if int(sliced_line[pos]) < int(sliced_line[pos + 1]):
                    del sliced_line[pos]
                    break
            else:
                break
        sliced_line = sliced_line[:digits]
        joltage += int(''.join(sliced_line))          
    return joltage

def load_input():
    filename = Path("input.txt")
    return filename.read_text().strip().splitlines()

if __name__ == "__main__":
    data = load_input()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))