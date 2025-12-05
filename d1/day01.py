from pathlib import Path

def part1(data):
    pos = 50
    count = 0

    for instruction in data:
        direction = instruction[0]
        value = int(instruction[1:])

        if direction == 'R':
            pos = (pos + value) % 100
        elif direction == 'L':
            pos = (pos - value) % 100
        if pos == 0:
            count += 1

    return count

def part2(data):
    pos = 50
    count = 0

    for instruction in data:
        direction = instruction[0]
        value = int(instruction[1:])

        if direction == 'R':
            count += (pos + value) // 100
            pos = (pos + value) % 100
        elif direction == 'L':
            if pos == 0:
                count += value // 100
            elif value >= pos:
                count += 1 + (value - pos) // 100
            pos = (pos - value) % 100

    return count

def load_input(day):
    filename = Path(f"d{day}/input.txt")
    return filename.read_text().strip().splitlines()

if __name__ == "__main__":
    day = 1
    data = load_input(day)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))