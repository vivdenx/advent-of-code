from aocd import get_data
from itertools import groupby

def calculate_total(data):
    total = []
    res = [[data[j][i] for j in range(len(data))] for i in range(len(data[0]))]
    for row in res:
        total.append(eval(row[-1].join(row[:-1])))
    return sum(total)


def solve_part2(data):
    total = []
    operators = data[-1].split()
    data = data[:-1]
    res = ["".join([data[j][i] for j in range(len(data))]).strip() for i in range(len(data[0]))]
    res = [list(g) for k, g in groupby(res, key=bool) if k]

    for operator, values in zip(operators, res):
        total.append(eval(operator.join(values)))

    return sum(total)


if __name__ == "__main__":
    test = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """.splitlines()
    assert calculate_total([line.split() for line in test if line.strip()]) == 4277556, "Test (pt 1) failed"
    assert solve_part2(test) == 3263827, "Test (pt 2) failed"

    data = get_data(year=2025, day=6)
    data = data.splitlines()
    result = calculate_total([line.split() for line in data if line.strip()])  
    print(result)

    result = solve_part2(data)
    print(result)