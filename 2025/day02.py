
"""Day 2: find IDs within ranges whose digits split into two equal halves."""


def load_input(path: str) -> list[str]:
    with open(path) as f:
        return f.read().split(",")
    

def is_invalid(value: str) -> bool:
    if len(value) % 2 == 0:
        beginning = value[:len(value)//2]
        end = value[len(value)//2:]
        return beginning == end
    return False


def find_invalid_ids(ranges: list[str]) -> list[str]:
    invalid_ids = []
    
    for id_range in ranges:
        start, end = map(int, id_range.split("-"))
        for value in range(start, end + 1):
            if is_invalid(str(value)):
                invalid_ids.append(value)

    return sum(invalid_ids)


if __name__ == "__main__":
    test = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    assert find_invalid_ids(test.split(',')) == 1227775554, "test case failed"

    data = load_input("./data/day02.txt")
    result = find_invalid_ids(data)
    print(result)