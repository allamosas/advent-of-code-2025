from pathlib import Path

def part1(data):
    # TODO: resolver parte 1
    return None

def part2(data):
    # TODO: resolver parte 2
    return None

def load_input():
    filename = Path("input.txt")
    return filename.read_text().strip().splitlines()

if __name__ == "__main__":
    data = load_input()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))