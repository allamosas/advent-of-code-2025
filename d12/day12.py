from pathlib import Path

def part1(data):
    shapes, regions = parse_input(data)
    total = 0
    for w, h, counts in regions:
        region_area = w * h
        pieces_area = sum(counts[i] * shapes[i] for i in range(len(shapes)))
        if pieces_area <= region_area:
            total += 1

    return total

def part2(data):
    # WHAAAAAAAAAAAAAAT
    return None

def parse_input(data):
    shapes = []
    regions = []
    i = 0

    # Leer formas
    while i < len(data):
        line = data[i].strip()
        if not line:
            i += 1
            continue

        if "x" in line:
            break

        if ":" in line:
            i += 1
            shape_lines = []
            while i < len(data) and data[i] and ":" not in data[i] and "x" not in data[i]:
                shape_lines.append(data[i])
                i += 1

            area = sum(row.count('#') for row in shape_lines)
            shapes.append(area)
        else:
            i += 1

    # Leer regiones
    while i < len(data):
        line = data[i].strip()
        if "x" in line:
            dims, counts = line.split(":")
            w, h = map(int, dims.split("x"))
            counts = list(map(int, counts.split()))
            regions.append((w, h, counts))
        i += 1

    return shapes, regions

def load_input(day):
    filename = Path(f"d{day}/input.txt")
    return filename.read_text().strip().splitlines()

if __name__ == "__main__":
    day = 12
    data = load_input(day)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
