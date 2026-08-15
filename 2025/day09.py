from aocd import get_data, submit
from itertools import combinations
from math import comb
from tqdm import tqdm

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

def get_grid_line_points(x0, y0, x1, y1):
    x_min, x_max = min(x0, x1), max(x0, x1)
    y_min, y_max = min(y0, y1), max(y0, y1)

    coordinates = []
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            coordinates.append((x, y))
            
    return coordinates


def solve2(red_points):
    max_size = 0
    green_points = []

    for i in tqdm(range(len(red_points))):
        xa, ya = [int(x) for x in red_points[i].split(',')]
        try:
            xb, yb = [int(x) for x in red_points[i+1].split(',')]
        except:
            xb, yb = [int(x) for x in red_points[0].split(',')]

        points = get_grid_line_points(xa, ya, xb, yb)
        for point in points:
            green_points.append(point)

    green_points = sorted(green_points, key = lambda x: (x[1], x[0]))

    print(green_points)
    break
    previous_y = 0
    start_x = 0
    for x, y in green_points:
        if y != previous_y:
            previous_y = y
            start_x = x
        else:
            for i in range(start_x+1, x):
                green_points.append((i, y))     
    
    all_points = green_points
    for line in red_points:
        x, y = line.split(',')
        all_points.append((int(x), int(y)))

    all_points = set(all_points)

    n = len(red_points)
    total = comb(n, 2)

    for i, j in tqdm(combinations(range(len(red_points)), 2), total=total):
        xa, ya = [int(x) for x in red_points[i].split(',')]
        xb, yb = [int(x) for x in red_points[j].split(',')]
    
        x = abs(xa-xb)+1
        y = abs(ya-yb)+1
    
        if x * y > max_size:
            points = get_grid_line_points(xa, ya, xb, yb)
            if all(point in all_points for point in points):
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
    assert solve2(test) == 24, "test case (pt 2) failed"

    data = get_data(year=2025, day=9).splitlines()
    res = solve1(data)
    #submit(res, year=2025, day=9, part='a')

    res = solve2(data)
    print(res)