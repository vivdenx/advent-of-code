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
                indices.update([index - 1, index + 1])

        for i in indices:
            line[i] = "|"
    return splits
        

def solve_part2(data):
    start_position = {data[0].index("S"): 1}

    for line in data[1:]: 
        next = {}
        line = [c for c in line]

        for position, count in start_position.items():
            if line[position] == "^":
                if next.get(position-1):
                    next[position-1] += count
                else:
                    next[position-1] = count
                if next.get(position+1):
                    next[position+1] += count
                else:
                    next[position+1] = count
            else:
                if next.get(position):
                    next[position] += count
                else:
                    next[position] = count

        start_position = next

    return sum(v for v in start_position.values())
   



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
    #submit(solve1, part="a", day=7, year=2025)

    solve2 = solve_part2(data)
    submit(solve2, part="b", day=7, year=2025)

    