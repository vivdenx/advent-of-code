def load_input(path: str) -> list[str]:
    with open(path) as f:
        return f.read().splitlines()

    
def check_pick_up(grid: list[str], start_width: int) -> int:
    if start_width == len(grid[0]):
        padded_grid = [start_width * "."] + grid + [start_width * "."]
        padded_grid = ['.' + row + '.' for row in padded_grid]
    else:
        padded_grid = grid

    memory = [list(row) for row in padded_grid]
    
    counter = 0
    for i, row in enumerate(padded_grid):
        for j, value in enumerate(row):
            if value == 'x':
                memory[i][j] = '.'
            if value != "@":
                continue
            if i == 0 or j == 0 or i == len(padded_grid) - 1 or j == len(row) - 1:
                continue

            first_row_count = padded_grid[i-1][j-1:j+2].count('@')
            second_row_count = padded_grid[i][j-1:j+2].count('@') - 1
            third_row_count = padded_grid[i+1][j-1:j+2].count('@')

            if first_row_count + second_row_count + third_row_count < 4:
                counter += 1
                memory[i][j] = 'x'

    return counter, memory
    
    
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
    assert check_pick_up(test, len(test[0]))[0] == 13

    data = load_input("./data/day04.txt")
    result = check_pick_up(data, len(data[0]))
    print(result[0])

    test_grid = test
    test_counter = 1
    start_width = len(test_grid[0]) 

    full_counter = 0
    while test_counter != 0:
        test_counter, test_grid = check_pick_up(test_grid, start_width)
        full_counter += test_counter
    assert full_counter == 43

    grid_copy = data
    counter = 1
    start_width = len(grid_copy[0])

    all_rolls = 0
    while counter != 0:
        counter, grid_copy = check_pick_up(grid_copy, start_width)
        all_rolls += counter
    print(all_rolls)

        