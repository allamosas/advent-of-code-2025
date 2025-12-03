from pathlib import Path

def part1(data):
    total = 0
    for interval in data:
        lower, upper = map(int, interval.split("-"))
        for number in range(lower, upper + 1):
            str_num = str(number)
            if str_num[:len(str_num)//2] == str_num[len(str_num)//2:]:
                total += number          
    return total

def part2(data):
    total = 0
    for interval in data:
        lower, upper = map(int, interval.split("-"))
        for number in range(lower, upper + 1):
            str_num = str(number)
            for npos in range(1, len(str_num)):
                if (is_reiterative(str_num[:npos], str_num)):
                    total += number
                    break
    return total

def is_reiterative(substring, str_num):
    len_sub = len(substring)
    for start in range(0, len(str_num), len_sub):
        if str_num[start:start + len_sub] != substring:
            return False
    return True

def load_input():
    filename = Path("input.txt")
    return filename.read_text().strip().split(",")

if __name__ == "__main__":
    data = load_input()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))