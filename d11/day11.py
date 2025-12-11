from pathlib import Path
from functools import lru_cache

#    __                               __                           
#   / /______  __    _________ ______/ /_  ___                     
#  / / ___/ / / /   / ___/ __ `/ ___/ __ \/ _ \                    
# / / /  / /_/ /   / /__/ /_/ / /__/ / / /  __/                    
#/_/_/   \__,_/____\___/\__,_/\___/_/ /_/\___/                     
#   ____ ____/_____/ _____     / /_  ______________________________
#  / __ `/ __ \/ _ \/ ___/    / __ \/ ___/ ___/ ___/ ___/ ___/ ___/
# / /_/ / /_/ /  __(__  )    / /_/ / /  / /  / /  / /  / /  / /    
# \__, /\____/\___/____/    /_.___/_/  /_/  /_/  /_/  /_/  /_/     
#/____/                                                                                                                

def part1(data):
    exits = 0
    for value in data['you']:  # antes 'svr'
        exits += search_tree(data, value)
    return exits

def part2(data):
    return count_routes(data, "svr")

def search_tree(data, start):
    @lru_cache(maxsize=None) # Se saca de la función
    def dfs(node):
        if node == "out":
            return 1
        total = 0
        for next_node in data[node]:
            total += dfs(next_node)
        return total
    return dfs(start)

def count_routes(data, start):
    @lru_cache(maxsize=None)
    def dfs(node, has_dac, has_fft):
        has_dac = has_dac or node == "dac"
        has_fft = has_fft or node == "fft"
        if node == "out":
            return int(has_dac and has_fft)

        total = 0
        for next_node in data[node]:
            total += dfs(next_node, has_dac, has_fft)
        return total

    total_routes = 0
    for nxt in data[start]:
        total_routes += dfs(nxt, False, False)
    return total_routes

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