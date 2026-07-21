"""Day 3: find the max x-digit joltage per battery bank, order-preserving."""


def load_input(path: str) -> list[str]:
    with open(path) as f:
        return f.read().splitlines()


# Old solution commented out due to speed constraints
#def get_max_two_digit_number(bank: str) -> int:
#    highest = 0
#    for i, first_digit in enumerate(bank):
#        for second_digit in bank[i+1:]:
#            number = int(first_digit + second_digit)
#            if number > highest:
#                highest = number
#    return highest


def get_highest_x_digit_number(bank: str, x: int) -> int:
    digits = []
    start = 0

    while len(digits) < x:
        remaining_needed = x - len(digits) - 1
        window = bank[start : len(bank) - remaining_needed]

        best_digit, best_index = 0, start
        for index, digit in enumerate(window):
            if int(digit) > best_digit:
                best_digit = int(digit)
                best_index = start + index

        digits.append(best_digit)
        start = best_index + 1

    return int("".join(str(d) for d in digits))


def get_maximum_joltage(banks: list[str], x: int) -> int:
    return sum(get_highest_x_digit_number(bank, x) for bank in banks)


if __name__ == "__main__":
    test = """987654321111111
811111111111119
234234234234278
818181911112111""".splitlines()

    # Tests
    assert get_maximum_joltage(test, x=2) == 357
    assert sum(get_highest_x_digit_number(bank, x=12) for bank in test) == 3121910778619

    data = load_input("./data/day03.txt")
    part1 = get_maximum_joltage(data, x=2)
    part2 = get_maximum_joltage(data, x=12)
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")