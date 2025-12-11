from pathlib import Path
from functools import lru_cache

def part1(data):
    exits = 0
    for value in data['you']:
        exits += search_tree(data, value)
    return exits

def part2(data):
    # TODO: resolver parte 2
    return None

def search_tree(data, value, ttl=20):
    if value == 'out':
        print(f"Found exit in {20 - ttl} steps")
        return 1
    if ttl <= 0:
        return 0
    
    total_exits = 0
    for next_value in data[value]:
        total_exits += search_tree(data, next_value, ttl-1)
    return total_exits

def load_input(day):
    filename = Path(f"d{day}/input.txt")
    lines = filename.read_text().strip().splitlines()
    data = {}
    for line in lines:
        key, values = line.split(":")
        key = key.strip()
        values = values.strip().split()
        data[key] = values
    return data

if __name__ == "__main__":
    day = 11
    data = load_input(day)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))