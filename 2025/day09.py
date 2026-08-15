from aocd import get_data, submit
from itertools import combinations
import math


def solve1(data):
    max_size = 0
    for i, j in combinations(range(len(data)), 2):
        xa, ya = [int(x) for x in data[i].split(',')]
        xb, yb = [int(x) for x in data[j].split(',')]

        x = abs(xa-xb)+1
        y = abs(ya-yb)+1

        if x * y > max_size:
            max_size = x*y

    return max_size

if __name__ == "__main__":
    test = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3""".splitlines()

    assert solve1(test) == 50, "test case (pt 1) failed"
    data = get_data(year=2025, day=9).splitlines()
    res = solve1(data)

    submit(res, year=2025, day=9, part='a')