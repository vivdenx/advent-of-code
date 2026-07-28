def parse_input(text):
    """Parse the puzzle input into a list of (start, end) ranges and available IDs."""
    ranges_block, available_block = text.split('\n\n')

    ranges = []
    for line in ranges_block.splitlines():
        start, end = line.split('-')
        ranges.append((int(start), int(end)))

    available_ids = [int(x) for x in available_block.splitlines()]
    return ranges, available_ids


def merge_ranges(ranges):
    """Merge overlapping or adjacent (start, end) ranges into a minimal set."""
    merged = []
    for start, end in sorted(ranges):
        if merged and start <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    return merged


def count_fresh(available_ids, ranges):
    """Count how many available IDs fall within any of the given ranges."""
    return sum(
        any(start <= id_ <= end for start, end in ranges)
        for id_ in available_ids
    )


def total_range_size(ranges):
    """Sum the sizes of a list of (start, end) inclusive ranges."""
    return sum(end - start + 1 for start, end in ranges)


def solve(text):
    ranges, available_ids = parse_input(text)

    fresh_count = count_fresh(available_ids, ranges)
    print(fresh_count)

    merged = merge_ranges(ranges)
    print(total_range_size(merged))


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
    solve(test)

    with open('./data/day05.txt') as f:
        data = f.read()

    solve(data)