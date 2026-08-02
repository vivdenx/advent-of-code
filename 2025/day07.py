from aocd import get_data, submit


def solve_part1(data):
    splits = 0
    indices = set()
    
    for line in data:
        line = [c for c in line]
        if "S" in line:
            indices.add(line.index("S"))

        copy = indices.copy()
        for index in copy:
            if line[index] == "^":
                splits += 1
                indices.remove(index)
                for i, value in enumerate(line):
                    if value == "^":
                        indices.update([i - 1, i + 1])

        for i in indices:
            line[i] = "|"
    return splits
        


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

    data = get_data(year=2025, day=7).splitlines()
    solve1 = solve_part1(data)
    submit(solve1, part="a", day=7, year=2025)

    