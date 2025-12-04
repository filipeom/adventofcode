def safe_input():
    try:
        return input()
    except:
        return None

def joltage_part_one(batteries: str):
    n = len(batteries)
    max_joltage = -1
    for i in range(n):
        d = int(batteries[i])
        for j in range(i + 1, n):
            u = int(batteries[j])
            max_joltage = max(max_joltage, d * 10 + u)
    return max_joltage

def joltage_part_two(batteries: str) -> int:
    return 0

def main():
    part_one: list[int] = []
    part_two: list[int] = []

    while line := safe_input():
        part_one.append(joltage_part_one(line))
        part_two.append(joltage_part_two(line))

    print(sum(part_one), sum(part_two))

main()
