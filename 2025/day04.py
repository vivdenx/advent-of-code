def load_input(path: str) -> list[str]:
    with open(path) as f:
        return f.read().splitlines()
    
def check_pick_up(grid):
    length = len(grid)
    padded_grid = [length * "."] + grid + [length * "."]
    padded_grid = ['.' + row + '.' for row in padded_grid]
    
    counter = 0
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value == "@":
                if i != 0 and j != 0 and i != len(grid) - 1 and j != len(grid) - 1:
                    first_row_count = grid[i-1][j-1:j+2].count('@')
                    second_row_count = grid[i][j-1:j+2].count('@') - 1
                    third_row_count = grid[i+1][j-1:j+2].count('@')

                    print(first_row_count)
                    print(second_row_count)
                    print(third_row_count)
                    print()

                    if sum([first_row_count, second_row_count, third_row_count]) < 4:
                        counter += 1

    print(counter)
    
    
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
    print(test)
    check_pick_up(test)