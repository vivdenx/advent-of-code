from aocd import get_data, submit
import math
from itertools import combinations


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_components = n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # path halving
            x = self.parent[x]
        return x

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False  # already connected, no-op
        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        self.size[rx] += self.size[ry]
        self.num_components -= 1
        return True

    def component_sizes(self):
        sizes = {}
        for x in range(len(self.parent)):
            root = self.find(x)
            sizes[root] = sizes.get(root, 0) + 1
        return list(sizes.values())


def parse_points(data):
    return [tuple(int(v) for v in line.split(',')) for line in data]


def find_edges(points, max_connections=None):
    edges = []
    for i, j in combinations(range(len(points)), 2):
        d = math.dist(points[i], points[j])
        edges.append((d, i, j))

    edges.sort(key=lambda item: item[0])

    if max_connections:
        return edges[:max_connections]
    return edges


def solve1(data, max_connections=None):
    points = parse_points(data)
    edges = find_edges(points, max_connections)

    uf = UnionFind(len(points))
    for _, i, j in edges:
        uf.union(i, j)

    sizes = sorted(uf.component_sizes(), reverse=True)
    return math.prod(sizes[:3])


def solve2(data):
    points = parse_points(data)
    edges = find_edges(points)

    uf = UnionFind(len(points))
    for _, i, j in edges:
        uf.union(i, j)
        if uf.num_components == 1:
            return points[i][0] * points[j][0]


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
    submit(res, year=2025, day=8, part='a')
    
    res = solve2(data)
    submit(res, year=2025, day=8, part='b')