from pathlib import Path

def part1(data):
    grid = list_to_matrix(data)
    accesible_rolls = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "@":
                if look_around(grid, row, col) < 4:
                    accesible_rolls += 1
    return accesible_rolls

def part2(data):
    grid = list_to_matrix(data)
    accesible_rolls = 0
    latest = -1

    while(latest != accesible_rolls):
        latest = accesible_rolls
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "@":
                    if look_around(grid, row, col) < 4:
                        grid[row][col] = "x"
                        accesible_rolls += 1        
    return accesible_rolls

def list_to_matrix(data):
    rows = [list(s) for s in data]
    return rows

def look_around(grid, row, col):
    directions = [(-1, -1), (0, -1), (1, -1), (-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0)]  #NW, N, NE, SW, S, SE, W, E
    roll_counter = 0
    for dc, dr in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            if grid[r][c] == "@":
                roll_counter += 1
    return roll_counter

def load_input(day):
    filename = Path(f"d{day}/input.txt")
    return filename.read_text().strip().splitlines()

if __name__ == "__main__":
    day = 4
    data = load_input(day)
    print("Part 1:", part1(data))    
    print("Part 2:", part2(data))