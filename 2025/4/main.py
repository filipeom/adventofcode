def safe_input():
    try:
        return input()
    except:
        return None

def parse_grid() -> list[list[int]]:
    grid: list[list[int]] = []
    while line := safe_input():
        row: list[int] = []
        for c in line:
            if c == '.':
                row.append(0)
            else:
                assert (c == '@')
                row.append(1)
        grid.append(row)

    return grid

def can_remove(grid: list[list[int]], i: int, j: int) -> bool:
    count = 0
    has_left = j > 0
    has_right = j < len(grid[i]) - 1
    has_top = i > 0
    has_bot = i < len(grid) - 1

    if has_left:
        count += grid[i][j - 1]

    if has_right:
        count += grid[i][j + 1]

    if has_top:
        count += grid[i - 1][j]
        if has_left:
            count += grid[i - 1][j - 1]
        if has_right:
            count += grid[i - 1][j + 1]

    if has_bot:
        count += grid[i + 1][j]
        if has_left:
            count += grid[i + 1][j - 1]
        if has_right:
            count += grid[i + 1][j + 1]

    return count < 4

def part_one(grid: list[list[int]]):
    m, n = len(grid), len(grid[0])
    ans = 0
    for i in range(m):
        for j in range(n):
            # If it's not a roll continue
            if grid[i][j] == 0:
                continue

            if can_remove(grid, i, j):
                ans += 1
    print(ans)

def part_two(grid: list[list[int]]):
    m, n = len(grid), len(grid[0])
    ans = 0
    while True:
        to_remove: list[tuple[int, int]] = []

        # Find which we can remove
        for i in range(m):
            for j in range(n):
                # If it's not a roll continue
                if grid[i][j] == 0:
                    continue

                if can_remove(grid, i, j):
                    to_remove.append((i, j))

        # If nothing we end
        num_to_remove = len(to_remove)
        if num_to_remove == 0:
            break

        # Inc ans
        ans += num_to_remove

        # Remove
        for (i, j) in to_remove:
            grid[i][j] = 0

    print(ans)

grid = parse_grid()
part_one(grid)
part_two(grid)
