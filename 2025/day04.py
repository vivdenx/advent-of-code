def load_input(path: str) -> list[str]:
    with open(path) as f:
        return f.read().splitlines()
    
def check_pick_up(grid):
    length = len(grid)
    padded_grid = [length * "."] + grid + [length * "."]
    padded_grid = ['.' + row + '.' for row in padded_grid]
    
    counter = 0
    for i, row in enumerate(padded_grid):
        for j, value in enumerate(row):
            if value == "@":
                if all([i != 0, j != 0, i != len(padded_grid) - 1, j != len(padded_grid) - 1]):
                    first_row_count = padded_grid[i-1][j-1:j+2].count('@')
                    second_row_count = padded_grid[i][j-1:j+2].count('@') - 1
                    third_row_count = padded_grid[i+1][j-1:j+2].count('@')

                    if sum([first_row_count, second_row_count, third_row_count]) < 4:
                        counter += 1
    return counter
    
    
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
    data = load_input("./data/day04.txt")
    result = check_pick_up(data)
    print(result)