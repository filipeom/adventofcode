dial = 50
part_one = 0
part_two = 0

def safe_input():
    try:
        return input()
    except:
        return None

while line := safe_input():
    direction = line[0]
    distance = int(line[1:])

    # Count how many times we would have to rotate
    part_two += distance // 100

    # Set the number to lowest offset
    distance = distance % 100

    if direction == "L":
        diff = dial - distance
    else:
        assert (direction == "R")
        diff = dial + distance

    # See if we crossed a zero
    if dial != 0 and (diff > 100 or diff < 0):
        part_two += 1

    dial = diff % 100

    if dial == 0:
        part_one += 1
        part_two += 1

print(part_one, part_two)
