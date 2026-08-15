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

def solve2(red_points):
    max_size = 0
    green_points = []

    for i in range(len(red_points)):
        xa, ya = [int(x) for x in red_points[i].split(',')]
        try:
            xb, yb = [int(x) for x in red_points[i+1].split(',')]
        except:
            xb, yb = [int(x) for x in red_points[0].split(',')]

        if xa < xb:
            for i in range(xa+1, xb):
                green_points.append((i, ya))
        if xa > xb:
            for i in range(xb+1, xa):
                green_points.append((i, ya))

        if ya < yb:
            for i in range(ya+1, yb):
                green_points.append((xa, i))
        if ya > yb:
            for i in range(yb+1, ya):
                green_points.append((xa, i))

    green_points = sorted(green_points, key = lambda x: (x[1], x[0]))

    previous_y = 0
    start_x = 0
    for x, y in green_points:
        if y != previous_y:
            previous_y = y
            start_x = x
        else:
            print(start_x, previous_y)
            for i in range(start_x+1, x):
                if (i, y) not in green_points:
                    green_points.append((i, y))     
    
    green_points = sorted(green_points, key = lambda x: (x[1], x[0]))
    print(green_points)

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
    solve2(test)

    data = get_data(year=2025, day=9).splitlines()
    res = solve1(data)
    #submit(res, year=2025, day=9, part='a')