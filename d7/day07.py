from pathlib import Path
from functools import lru_cache


grid = []

def part1(data):
    global grid
    grid = [list(line) for line in data]  # Convertir cada línea en una lista de caracteres
    start = (0, grid[0].index('S'))  # Encontrar la posición inicial 'S'
    manyfolds = manyfold_loop(start)
    return manyfolds

def part2(data):
    global grid
    grid = [list(line) for line in data]  # Convertir cada línea en una lista de caracteres
    start = (0, grid[0].index('S'))  # Encontrar la posición inicial 'S'
    manyfolds = manyfold_loop(start)
    return manyfolds

@lru_cache(maxsize=128)
def manyfold_loop(pos):
    global grid
    if pos[0] == len(grid):  # Si hemos llegado al final del grid
        return 1    
    directions = [(1, 0), (0, -1), (0, 1)] # Down, Left, Right
    if grid[pos[0]][pos[1]] == '^': # Si manyfold
        return manyfold_loop(add_pos(pos, directions[1])) + manyfold_loop(add_pos(pos, directions[2]))   
    else:
        grid[pos[0]][pos[1]] = '|'
        return manyfold_loop(add_pos(pos, directions[0]))

def add_pos(pos, direction):
    return (pos[0] + direction[0], pos[1] + direction[1])

def print_grid(grid):
    for row in grid:
        print(''.join(row))
    print()

def load_input(day):
    filename = Path(f"d{day}/input.txt")
    return filename.read_text().strip().splitlines()

if __name__ == "__main__":
    day = 7
    data = load_input(day)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))