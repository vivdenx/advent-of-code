"""Day 3: find the max 2-digit joltage per battery bank, order-preserving."""


def load_input(path: str) -> list[str]:
    with open(path) as f:
        return f.read().splitlines()
    

def get_max_two_digit_number(bank: str) -> int:
    highest = 0
    for i, first_digit in enumerate(bank):
        for second_digit in bank[i+1:]:
            number = int(first_digit + second_digit)
            if number > highest:
                highest = number
    return highest


def get_highest_x_digit_number(bank: str, x: int) -> int:
    numbers = []
    i = 0

    while len(numbers) < x:
        highest = 0
        original_index = i
        for index, digit in enumerate(bank[i:len(bank)-x+len(numbers)+1]):
            if int(digit) > highest:
                i = index + original_index
                highest = int(digit)
        numbers.append(highest)
        i += 1

    numbers = ''.join(str(n) for n in numbers)
    return int(numbers)        

def get_maximum_joltage(banks: list[str], x: int) -> int:
    return sum(get_highest_x_digit_number(bank, x) for bank in banks)
                    
    
if __name__ == "__main__":
    test = """987654321111111
811111111111119
234234234234278
818181911112111"""
    test = test.splitlines()
    assert get_maximum_joltage(test, 2) == 357

    data = load_input("./data/day03.txt")
    result = get_maximum_joltage(data, 2)
    
    assert sum(get_highest_x_digit_number(bank, x=12) for bank in test) == 3121910778619
    result = get_maximum_joltage(data, x=12)
    print(result)
