def safe_input() -> str | None:
    try:
        return input()
    except:
        return None

def parse() -> list[list[str]]:
    grid: list[list[str]] = []
    while line := safe_input():
        line = line.strip().split()
        grid.append(line)
    return grid

def puzzle_1():
    grid = parse()
    n, m = len(grid), len(grid[0])
    result = 0
    for j in range(m):
        op = grid[n - 1][j]
        acc: int = 1 if op == '*' else 0
        for i in range(n - 1):
            if op == '*':
                acc *= int(grid[i][j])
            else:
                acc += int(grid[i][j])
        result += acc
    print(result)

def parse2() -> list[str]:
    result: list[str] = []
    while line := safe_input():
        print(line)
        result.append(line)
    return result

def puzzle_2():
    grid = parse2()
    n, m = len(grid), len(grid[0]) - 1
    result = 0
    column: list[int] = []
    while m >= 0:
        num: list[str] = []
        for i in range(n - 1):
            elt = grid[i][m]
            if elt != " ":
                num.append(elt)

        number = int(''.join(num))
        column.append(number)

        if grid[n - 1][m] == '*':
            acc = 1
            for elt in column:
                acc *= elt
            result += acc
            column.clear()
            m -= 2
        elif grid[n - 1][m] == '+':
            result += sum(column)
            column.clear()
            m -= 2
        else:
            m -= 1
    print(result)

# puzzle_1()
puzzle_2()
