def load_input(path: str) -> list[str]:
    with open(path) as f:
        return f.read().splitlines()

    
def check_pick_up(grid):
    width = len(grid[0])
    padded_grid = [width * "."] + grid + [width * "."]
    padded_grid = ['.' + row + '.' for row in padded_grid]
    
    counter = 0
    for i, row in enumerate(padded_grid):
        for j, value in enumerate(row):
            if value != "@":
                continue
            if i == 0 or j == 0 or i == len(padded_grid) - 1 or j == len(row) - 1:
                continue

            first_row_count = padded_grid[i-1][j-1:j+2].count('@')
            second_row_count = padded_grid[i][j-1:j+2].count('@') - 1
            third_row_count = padded_grid[i+1][j-1:j+2].count('@')

            if first_row_count + second_row_count + third_row_count < 4:
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
    assert check_pick_up(test) == 13

    data = load_input("./data/day04.txt")
    result = check_pick_up(data)
    print(result)