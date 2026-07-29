"""Day 1: track position on a circular dial (0-99) based on L/R turns."""

DIAL_MIN = 0
DIAL_MAX = 99
DIAL_SIZE = DIAL_MAX - DIAL_MIN + 1  # 100
START_POSITION = 50


def load_input(path: str) -> list[str]:
    with open(path) as f:
        return f.read().splitlines()


def parse_turn(turn: str) -> tuple[int, int]:
    """Parse a turn like 'L68' into a (step, amount) pair, where step is +1 or -1."""
    direction, amount = turn[0], int(turn[1:])
    step = -1 if direction == "L" else 1
    return step, amount


def count_zero_landings(turns: list[str]) -> int:
    """Count how many turns end with the dial exactly on 0."""
    position = START_POSITION
    zero_landings = 0

    for turn in turns:
        step, amount = parse_turn(turn)
        position = (position + step * amount) % DIAL_SIZE

        if position == 0:
            zero_landings += 1

    return zero_landings


def count_all_zero_crossings(turns: list[str]) -> int:
    """Count every time the dial passes over or lands on 0, including
    multiple wraps within a single turn."""
    position = START_POSITION
    zero_landings = 0

    for turn in turns:
        step, amount = parse_turn(turn)

        for _ in range(amount):
            position = (position + step) % DIAL_SIZE
            if position == 0:
                zero_landings += 1

    return zero_landings


if __name__ == "__main__":
    test = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
    assert count_zero_landings(test) == 3, "test case failed"
    assert count_all_zero_crossings(test) == 6, "test case (pt 2) failed"

    data = load_input("./data/day01.txt")
    print(count_zero_landings(data))
    print(count_all_zero_crossings(data))