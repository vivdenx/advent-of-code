"""Day 3: find the max 2-digit joltage per battery bank, order-preserving."""


def load_input(path: str) -> list[str]:
    with open(path) as f:
        return f.read().split("\n")
    

def get_max_two_digit_number(bank: str) -> int:
    highest = 0
    for i, first_digit in enumerate(bank):
        for second_digit in bank[i+1:]:
            number = int(first_digit + second_digit)
            if number > highest:
                highest = number
    return highest


def get_maximum_joltage(banks: list[str]) -> int:
    return sum(get_max_two_digit_number(bank) for bank in banks)
                    
    
if __name__ == "__main__":
    test = """987654321111111
811111111111119
234234234234278
818181911112111"""
    assert get_maximum_joltage(test.split('\n')) == 357

    data = load_input("./data/day03.txt")
    result = get_maximum_joltage(data)
    print(result)