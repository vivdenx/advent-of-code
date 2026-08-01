from aocd import get_data

def calculate_total(data):
    total = []
    res = [[data[j][i] for j in range(len(data))] for i in range(len(data[0]))]
    for row in res:
        if row[-1] == "*":
            total.append(eval("*".join(row[:-1])))
        elif row[-1] == "+":
            total.append(eval("+".join(row[:-1])))
    return sum(total)


if __name__ == "__main__":
    test = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """
    test = [line.split() for line in test.splitlines() if line.strip()]
    assert calculate_total(test) == 4277556, "Test failed"

    data = get_data(year=2025, day=6)
    data = [line.split() for line in data.splitlines() if line.strip()]
    result = calculate_total(data)  
    print(result)