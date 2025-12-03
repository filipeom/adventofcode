def is_invalid_part_one(n : str) -> bool:
    n_len = len(n)

    if n_len % 2 != 0:
        return False

    mid = n_len // 2
    return n[:mid] == n[mid:]

def is_invalid_part_two(n : str) -> bool:
    n_len = len(n)
    for width in range(1, n_len // 2 + 1):
        # A pattern width must devide n_len
        if n_len % width != 0:
            continue

        pattern = n[:width]
        match_count = 0
        for i in range(0, n_len, width):
            segment = n[i:i + width]
            if segment != pattern:
                match_count = 0
                break
            match_count += 1

        if match_count >= 2:
            return True

    return False

def main():
    line = input()
    ranges = line.split(",")

    part_one: list[int] = []
    part_two: list[int] = []

    for r in ranges:
        low, high = map(int, r.split("-"))
        for i in range(low, high + 1):
            i_str = str(i)
            if is_invalid_part_one(i_str):
                part_one.append(i)

            if is_invalid_part_two(i_str):
                part_two.append(i)

    print(sum(part_one), sum(part_two))

main()
