from aocd import get_data, submit
import math
import numpy as np


def calculate_distance(point_a, point_b):
    point_a = [int(x) for x in point_a.split(',')]
    point_b = [int(x) for x in point_b.split(',')]

    return math.dist(point_a, point_b)


def solve1(data, max_connections=10):
    connections = []
    while len(connections) < max_connections: 
        minimum = float('inf')
        closest = ''
        for point_a in data:
            for point_b in data:
                if point_a != point_b and (point_a, point_b) not in connections and (point_b, point_a) not in connections:
                    distance = calculate_distance(point_a, point_b)
                    if distance < minimum:
                        minimum = distance
                        closest = (point_a, point_b)

        connections.append(closest)

    print(connections)
        
    pass


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

    #solve1(test)
    test = [line.split(',') for line in test]
    test = [[int(x) for x in line] for line in test]
    solve_kdtree(test)

    data = get_data(year=2025, day=8).splitlines()
