from pathlib import Path
import numpy as np
from itertools import zip_longest

def part1(data): 
    grid = [line.split() for line in data] # Dividir cada línea en elementos separados por espacio
    grid = list(zip(*grid)) # Transponer la matriz para facilitar el acceso por columnas
    return sum_up(grid) # Sumar los resultados de cada fila usando la función sum_up

def part2(data): # Estos pavos son sunormales
    grid = list(zip_longest(*data, fillvalue="")) # Transponer la matriz rellenando con cadenas vacías para no perder datos
    grid = translate_sunormal(grid) # Traducir los caracteres sunormales a operadores matemáticos
    return sum_up(grid)

def translate_sunormal(grid): # Traducir los caracteres sunormales a operadores matemáticos
    translated_grid = []
    t_row = []
    op = None
    for row in grid:
        if ''.join(map(str, row)).replace(' ', '') == '':
            continue
        if row[-1] in ('+', '*'):
            if t_row:
                t_row.append(op)
                translated_grid.append(t_row)
            op = row[-1]
            t_row = [int(''.join(map(str, row[:-1])))]
        else:
            t_row.append(int(''.join(map(str, row))))
    if t_row:
        t_row.append(op)
        translated_grid.append(t_row)
    return translated_grid

def sum_up(grid):
    total = 0
    for row in grid: 
        operator = row[-1] # Último elemento de la fila es el operador
        nums = np.array(row[:-1], dtype=int) # Convertir los demás elementos a enteros
        if operator == '+': 
            total += int(nums.sum()) 
        elif operator == '*': 
            total += int(nums.prod()) 
    return total

def load_input(day):
    filename = Path(f"d{day}/input.txt")
    return filename.read_text().strip().splitlines()

if __name__ == "__main__":
    day = 6
    data = load_input(day)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))