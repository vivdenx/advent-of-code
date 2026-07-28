def load_input(test):
    ranges, available = test.split('\n\n')
    ranges = [e.split('-') for e in ranges.splitlines()]
    ranges = [(int(start), int(end)) for start, end in ranges]
    return ranges, available.splitlines()


def find_fresh_ingredients(data):
    ranges, available = load_input(data)
    ranges = sorted(ranges)

    counter = 0

    for id in available:
        if any(int(id) in range(start, end+1) for start, end in ranges):
            counter += 1

    print(counter)

    merged = []
    for start, end in ranges:
        if merged and start <= merged[-1][1] + 1:  # overlapping or adjacent
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))

    print(sum([len(range(start, end + 1)) for start, end in merged]))

    pass


if __name__ == "__main__":
    test = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""
    find_fresh_ingredients(test)

    with open('./data/day05.txt') as f:
        data = f.read()

    find_fresh_ingredients(data)