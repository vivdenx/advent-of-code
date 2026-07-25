def load_input(path: str) -> list[str]:
    with open(path) as f:
        return f.read().splitlines()
    
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
@.@.@@@.@."""
    data = load_input("./data/day04.txt")
    print(test)