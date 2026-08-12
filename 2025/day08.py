from aocd import get_data, submit
import math
import numpy as np
from collections import defaultdict
from itertools import combinations

def calculate_distance(point_a, point_b):
    point_a = [int(x) for x in point_a.split(',')]
    point_b = [int(x) for x in point_b.split(',')]

    return math.dist(point_a, point_b)


def solve1_v2(data, max_connections = 10):
    n = len(data)

    edges = []
    for i, j in combinations(range(n), 2):
        d = calculate_distance(data[i], data[j])
        edges.append((d, i, j))

    edges = sorted(edges, key=lambda item: item[0])[:max_connections]

    # Union Find algorithm...
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

    top3 = sorted(comp_sizes.values(), reverse=True)[:3]
    return math.prod(top3)
    

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

    assert solve1_v2(test) == 40, "test (pt 2) failed"

    test = [line.split(',') for line in test]
    test = [[int(x) for x in line] for line in test]

    data = get_data(year=2025, day=8).splitlines()
    res = solve1_v2(data, 1000)
    print(res)
    submit(res, year=2025, day=8)
