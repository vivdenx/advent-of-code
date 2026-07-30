"""Day 2: Find IDs within ranges whose digits split into two equal halves
(part 1) or consist of any repeated digit block (part 2).
"""

from pathlib import Path


def load_ranges(path: str) -> list[str]:
    """Read comma-separated 'start-end' ranges from a file."""
    return Path(path).read_text().strip().split(",")


def has_repeated_halves(value: str) -> bool:
    """True if `value` splits evenly into two identical halves."""
    if len(value) % 2 != 0:
        return False
    half = len(value) // 2
    return value[:half] == value[half:]


def has_repeated_block(value: str) -> bool:
    """True if `value` is made of a repeating digit block (any block size)."""
    n = len(value)
    for block_size in range(1, n // 2 + 1):
        if n % block_size == 0 and value[:block_size] * (n // block_size) == value:
            return True
    return False


def sum_matching_ids(ranges: list[str], part2: bool = False) -> int:
    """Sum every ID in the given ranges that matches the relevant rule."""
    is_match = has_repeated_block if part2 else has_repeated_halves

    total = 0
    for id_range in ranges:
        start, end = map(int, id_range.split("-"))
        for value in range(start, end + 1):
            if is_match(str(value)):
                total += value
    return total


TEST_INPUT = (
    "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,"
    "1698522-1698528,446443-446449,38593856-38593862,565653-565659,"
    "824824821-824824827,2121212118-2121212124"
)


def run_tests() -> None:
    test_ranges = TEST_INPUT.split(",")
    assert sum_matching_ids(test_ranges) == 1227775554, "test case pt 1 failed"
    assert sum_matching_ids(test_ranges, part2=True) == 4174379265, "test case pt 2 failed"


def main() -> None:
    run_tests()

    data = load_ranges("./data/day02.txt")
    print(sum_matching_ids(data))
    print(sum_matching_ids(data, part2=True))


if __name__ == "__main__":
    main()