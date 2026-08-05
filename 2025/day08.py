from aocd import get_data, submit
import math

def solve1(data):
    data = {index + 1: [int(i) for i in value.split(',')] for index, value in enumerate(data)}
    
    print(data)
    
    minimum = 100000
    for i in data:
        point_a = [int(x) for x in i.split(',')]
        for j in data:
            point_b = [int(x) for x in j.split(',')]
            if i != j:
                distance = math.dist(point_a, point_b)
                if distance < minimum:
                    minimum = distance

    print(minimum)
        
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

    solve1(test)

    data = get_data(year=2025, day=8).splitlines()
