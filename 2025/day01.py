DIAL_MIN = 0
DIAL_MAX = 99
START_POSITION = 50

def load_input(path: str) -> list[str]:
    with open(path) as f:
        return f.read().splitlines()


def count_zero_landings(turns: list[str]) -> int:
    position = START_POSITION
    zero_landings = 0

    for turn in turns:
        direction, amount = turn[0], int(turn[1:])

        if direction == "L":
            position -= amount
        elif direction == "R":
            position += amount

        while position > DIAL_MAX:
            position -= (DIAL_MAX + 1)
        while position < DIAL_MIN:
            position += (DIAL_MAX + 1)
        
        if position == 0:
            zero_landings += 1
    
    return zero_landings

if __name__ == "__main__":
    test = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
    assert count_zero_landings(test) == 3, "test case failed"

    data = load_input("./data/day01.txt")
    print(count_zero_landings(data))