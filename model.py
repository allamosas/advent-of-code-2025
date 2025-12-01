from pathlib import Path

def part1(data):
    # TODO: resolver parte 1
    return None

def part2(data):
    # TODO: resolver parte 2
    return None

def load_input(day):
    filename = Path("input") / f"day{day:02d}.txt"
    return filename.read_text().strip().splitlines()

if __name__ == "__main__":
    day = 1
    data = load_input(day)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
