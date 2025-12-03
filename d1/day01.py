from pathlib import Path

def part1(data):
    pos = 50
    count = 0
    
    for instruction in data:
        dir = instruction[0]
        value = int(instruction[1:])
        if dir =='R':
            pos += value

        if dir =='L':
            pos -= value

        pos = pos % 100
        
        if pos == 0:
            count += 1
    return count

def part2(data):
    pos = 50
    count = 0

    for instruction in data:
        dir = instruction[0]
        value = int(instruction[1:])
        if dir =='R':
            for step in range(value):
                pos += 1
                pos = pos % 100
                if pos == 0:
                    count += 1

        if dir =='L':
            for step in range(value):
                pos -= 1
                pos = pos % 100
                if pos == 0:
                    count += 1

    return count

def load_input():
    filename = Path("input.txt")
    return filename.read_text().strip().splitlines()

if __name__ == "__main__":
    data = load_input()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))