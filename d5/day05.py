from pathlib import Path
from intervaltree import IntervalTree, Interval

def part1(data):
    empty_line = data.index('')
    fresh_ids = data[:empty_line]
    ids = data[empty_line + 1:]

    fresh_ids = [tuple(map(int, r.split('-'))) for r in fresh_ids]
    fresh = 0
    for ingredient_id in ids:
        ingredient_id = int(ingredient_id)
        for r in fresh_ids:
            if r[0] <= ingredient_id <= r[1]:
                fresh += 1
                break
    
    return fresh

def part2(data):
    empty_line = data.index('')
    fresh_ids = data[:empty_line]
    fresh_ids = [tuple(map(int, r.split('-'))) for r in fresh_ids]

    fresh_ranges = IntervalTree() # Libreria para manejar rangos con complejidad O(n log n) y almacenamiento O(n)
    for a, b in fresh_ids: # Añadir intervalos al árbol
        fresh_ranges.addi(a, b + 1)
    fresh_ranges.merge_overlaps() # Unir intervalos que se solapan

    total = sum(interval.end - interval.begin for interval in fresh_ranges) # Calcular total de IDs frescos
    return total

def load_input(day):
    filename = Path(f"d{day}/input.txt")
    return filename.read_text().strip().splitlines()

if __name__ == "__main__":
    day = 5
    data = load_input(day)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))