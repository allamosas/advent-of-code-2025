from pathlib import Path
from functools import lru_cache

def part1(data):
    points = [tuple(map(int, line.split(','))) for line in data]
    area = find_area(points, part1=True)
    return area

def part2(data):
    points = [tuple(map(int, line.split(','))) for line in data]
    area = find_area(points, verbose=True)
    return area

def find_area(points, part1 = False, verbose=False):
    largest_area = 0
    for i, (x1, y1) in enumerate(points):
        if verbose:
            print(f"\rCalculando áreas para punto {i+1}/{len(points)}: ({x1}, {y1})", end='', flush=True)
        for j, (x2, y2) in enumerate(points):
            if i == j:
                continue
            if part1 or rect_valid((x1, y1), (x2, y2), points):
                area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
                if area > largest_area:
                    largest_area = area
                    if verbose:
                        print(f"  Nueva área mayor: {largest_area}")
    return largest_area
    
def point_in_area(px, py, x1, y1, x2, y2):
    minx, maxx = min(x1, x2), max(x1, x2)
    miny, maxy = min(y1, y2), max(y1, y2)
    return minx < px < maxx and miny < py < maxy

def segments_intersect(a, b, c, d):
    o1 = cross_product(a, b, c)
    o2 = cross_product(a, b, d)
    o3 = cross_product(c, d, a)
    o4 = cross_product(c, d, b)
    return o1*o2 < 0 and o3*o4 < 0

def cross_product(p, q, r): # Hoy he aprendido que el determinante de una matriz es cross product en inglés
    return (q[0]-p[0])*(r[1]-p[1]) - (q[1]-p[1])*(r[0]-p[0])

def rect_valid(p1, p2, polygon):
    x1, y1 = p1
    x2, y2 = p2
    # Comprobar que ningún otro punto está dentro
    for px, py in polygon:
        if (px, py) != p1 and (px, py) != p2:
            if point_in_area(px, py, x1, y1, x2, y2):
                return False

    # Comprobar intersección con aristas del polígono
    n = len(polygon)
    rect_edges = [
        ((x1, y1), (x1, y2)),
        ((x1, y2), (x2, y2)),
        ((x2, y2), (x2, y1)),
        ((x2, y1), (x1, y1)),
    ]

    for i in range(n):
        a = polygon[i]
        b = polygon[(i+1) % n]
        for re1, re2 in rect_edges:
            if segments_intersect(re1, re2, a, b):
                return False
    return True

def load_input(day):
    filename = Path(f"d{day}/input.txt")
    return filename.read_text().strip().splitlines()

if __name__ == "__main__":
    day = 9
    data = load_input(day)
    print("\nPart 1:", part1(data))
    print("\nPart 2:", part2(data))