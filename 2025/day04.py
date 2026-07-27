from pathlib import Path

def load_input(path: str) -> list[str]:
    return Path(path).read_text().splitlines()


def pad_grid(grid: list[str]) -> list[str]:
    border = "." * (len(grid[0]) + 2)
    return [border] + ['.' + row + '.' for row in grid] + [border]


def remove_rolls(grid: list[str]) -> tuple[int, list[str]]:
    """
    Remove every '@' that has less than 4 '@' neighbours.
    """
    height, width = len(grid), len(grid[0])
    new_grid = [list(row) for row in grid]
    removed = 0

    for i in range(1, height - 1):
        for j in range(1, width - 1):
            if grid[i][j] != '@':
                continue

            neighbors = (
                grid[i-1][j-1:j+2].count('@')
                + grid[i][j-1:j+2].count('@') - 1
                + grid[i+1][j-1:j+2].count('@')
            )

            if neighbors < 4:
                new_grid[i][j] = '.'
                removed += 1

    return removed, ["".join(row) for row in new_grid]


def count_total_removals(grid: list[str]) -> int:
    """Repeatedly remove lonely '@' until grid stabilizes"""
    grid = pad_grid(grid)
    total = 0
    while True:
        removed, grid = remove_rolls(grid)
        total += removed
        if removed == 0:
            break
    return total


def solve_part1(grid: list[str]) -> int:
    return remove_rolls(pad_grid(grid))[0]


def solve_part2(grid: list[str]) -> int:
    return count_total_removals(grid)

    
if __name__ == "__main__":
    test = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.""".splitlines()
    assert solve_part1(test) == 13
    assert solve_part2(test) == 43

    data = load_input("./data/day04.txt")
    print(solve_part1(data))
    print(solve_part2(data))