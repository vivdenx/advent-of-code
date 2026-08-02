from collections import defaultdict
from aocd import get_data, submit


def solve_part1(data):
    splits = 0
    positions = set()

    for line in data:
        if "S" in line:
            positions.add(line.index("S"))

        for position in positions.copy():
            if line[position] == "^":
                splits += 1
                positions.remove(position)
                positions.update([position - 1, position + 1])

    return splits
        

def solve_part2(data):
    timelines = {data[0].index("S"): 1}

    for line in data[1:]: 
        next_timelines = defaultdict(int)

        for position, count in timelines.items():
            if line[position] == "^":
                next_timelines[position-1] += count
                next_timelines[position+1] += count
            else:
                next_timelines[position] += count

        timelines = next_timelines

    return sum(timelines.values())
   

if __name__ == "__main__":
    test = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............""".splitlines()

    assert solve_part1(test) == 21, "Test (pt 1) failed"
    assert solve_part2(test) == 40, "Test (pt 2) failed"

    data = get_data(year=2025, day=7).splitlines()
    solve1 = solve_part1(data)
    submit(solve1, part="a", day=7, year=2025)

    solve2 = solve_part2(data)
    submit(solve2, part="b", day=7, year=2025)

    