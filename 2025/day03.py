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
    print(bank)

    while len(numbers) < x:
        highest = 0
        for index, digit in enumerate(bank[i:len(bank)-x+i+1]):
            if int(digit) > highest:
                i = index
                highest = int(digit)
                numbers.append(highest)

        #highest = max(d for d in bank[i:len(bank)-x+i+1])

        #numbers.append(highest)
        i += 1
        print(highest)
    print(numbers)
        

def get_maximum_joltage(banks: list[str]) -> int:
    return sum(get_max_two_digit_number(bank) for bank in banks)
                    
    
if __name__ == "__main__":
    test = """987654321111111
811111111111119
234234234234278
818181911112111"""
    test = test.splitlines()
    assert get_maximum_joltage(test) == 357

    data = load_input("./data/day03.txt")
    result = get_maximum_joltage(data)
    
    for bank in test:
        get_highest_x_digit_number(bank, x=2)
    #assert sum(get_highest_x_digit_number(bank, x=12) for bank in test.splitlines()) == 3121910778619
    print(result)

