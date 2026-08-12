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

    edges = sorted(edges, key=lambda item: item[0])

    groups = defaultdict()

    for _, i, j in edges[:max_connections]:
        key = [key for key,value in groups.items() if i in value or j in value]

        if key:
            if i in groups[key[0]]:
                groups[key[0]] += [j]
            else:
                groups[key[0]] += [i]

        else:
            res = 0
            if groups:
                res = max(groups, key=groups.get) + 1
            groups[res] = [i] + [j]

    length_dict = {key: len(value) for key, value in groups.items()}
    length_dict = dict(sorted(length_dict.items(), key=lambda item: item[1], reverse=True)[:3])

    result = math.prod(length_dict.values())
    return result



def solve1(data, max_connections=10):
    connections = defaultdict()
    connections_list = []

    while len(connections_list) < max_connections: 
        minimum = float('inf')
        closest = []
        for i in range(len(data)):
            for j in range(i+1, len(data)):
                if (data[i], data[j]) not in connections_list and (data[j], data[i]) not in connections_list:
                    distance = calculate_distance(data[i], data[j])
                    if distance < minimum:
                        minimum = distance
                        closest = (data[i], data[j])

        connections_list.append(closest)

        point_a, point_b = closest
        key = [key for key, value in connections.items() if point_a in value or point_b in value]

        if key:
            if point_a in connections[key[0]]:
                connections[key[0]] += [point_b]
            else:
                connections[key[0]] += [point_a]

        else:
            if connections:
                res = max(connections, key=connections.get) + 1
            else:
                res = 0

            connections[res] = [point_a] + [point_b]

    length_dict = {key: len(value) for key, value in connections.items()}
    length_dict = dict(sorted(length_dict.items(), key=lambda item: item[1], reverse=True)[:3])

    result = math.prod(length_dict.values())
    return result

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
