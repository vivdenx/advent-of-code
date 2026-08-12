from aocd import get_data, submit
import math
from itertools import combinations
import numpy as np

def calculate_distance(point_a, point_b):
    point_a = [int(x) for x in point_a.split(',')]
    point_b = [int(x) for x in point_b.split(',')]

    return math.dist(point_a, point_b)


def find_edges(data, max_connections=None):
    n = len(data)
        
    edges = []
    for i, j in combinations(range(n), 2):
        d = calculate_distance(data[i], data[j])
        edges.append((d, i, j))

    edges = sorted(edges, key=lambda item: item[0])

    if max_connections:
        return edges[:max_connections]
    return edges


def solve1(data, max_connections=None):
    edges = find_edges(data, max_connections)

    # Union Find algorithm...
    n = len(data)
    parent = list(range(n))
    size = [1] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]  # path halving
            x = parent[x]
        return x

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return
        # Only merge if they belong to different groups
        # Union by rank: attach smaller tree to larger tree
        if size[rx] < size[ry]:
            rx, ry = ry, rx
        parent[ry] = rx
        size[rx] += size[ry]

    for _, i, j in edges:
        union(i, j)

    comp_sizes = {}
    for i in range(n):
        root = find(i)
        comp_sizes[root] = comp_sizes.get(root, 0) + 1

    sort = sorted(comp_sizes.values(), reverse=True)
    return math.prod(sort[:3])


def solve2(data, max_connections=None):
    edges = find_edges(data, max_connections)
    
    # Union Find algorithm...
    n = len(data)
    parent = list(range(n))
    size = [1] * n
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]  # path halving
            x = parent[x]
        return x
    
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return
        # Only merge if they belong to different groups
        # Union by rank: attach smaller tree to larger tree
        if size[rx] < size[ry]:
            rx, ry = ry, rx
        parent[ry] = rx
        size[rx] += size[ry]
    
    for _, i, j in edges:
        union(i, j)
        if len({find(x) for x in range(n)}) == 1:
            x1, x2 = int(data[i].split(',')[0]), int(data[j].split(',')[0])
            return math.prod([x1, x2])
        



if __name__ == "__main__":
    test = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
""".splitlines()

    assert solve1(test, 10) == 40, "test (pt 1) failed"
    assert solve2(test) == 25272, "test (pt 2) failed"
    
    data = get_data(year=2025, day=8).splitlines()
    res = solve1(data, 1000)

    res = solve2(data)
    submit(res, year=2025, day=8)

