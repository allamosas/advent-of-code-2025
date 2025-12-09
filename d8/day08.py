from pathlib import Path
import numpy as np
from scipy.spatial.distance import pdist

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n
        self.count = n
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.count -= 1
        return True

def last_connection_scipy(points):
    # points: lista de tuplas (x,y,z)
    pts = np.array(points, dtype=int)
    n = len(points)
    
    # pdist devuelve el vector condensado de distancias (i<j)
    dvec = pdist(pts)               # length n*(n-1)/2
    order = np.argsort(dvec)        # Indices de pares por distancia ascendente

    iu = np.triu_indices(n, 1)
    dsu = DSU(n)

    last_pair = None
    for idx in order:
        i = iu[0][idx]
        j = iu[1][idx]
        if dsu.union(i, j):
            last_pair = (i, j)
            last_dist = dvec[idx]
            if dsu.count == 1:
                break

    i, j = last_pair
    x_product = points[i][0] * points[j][0]
    return x_product

def part1(data):
    points = [tuple(map(int, line.split(','))) for line in data]
    #print(solve(points, K=1000))

def part2(data):
    points = [tuple(map(int, line.split(','))) for line in data]
    return last_connection_scipy(points)

def load_input(day):
    filename = Path(f"d{day}/input.txt")
    return filename.read_text().strip().splitlines()

if __name__ == "__main__":
    day = 8
    data = load_input(day)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))