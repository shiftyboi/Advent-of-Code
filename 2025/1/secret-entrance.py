import sys, math

def sign(x):
    return -1 if x < 0 else 1

def part1():
    zeroes = 0
    pointing = 50
    with open(sys.argv[1]) as f:
        rotations = f.read().split()

    for item in rotations:
        delta = (1 - 2*(item[0] == 'L')) * int(item[1:])

        pointing = (pointing + delta) % 100
        if not pointing:
            zeroes += 1

    return zeroes

def part2():
    zeroes = 0
    pointing = 50
    with open(sys.argv[1]) as f:
        rotations = f.read().split()

    for item in rotations:
        start_point = pointing
        delta = (1 - 2*(item[0] == 'L')) * int(item[1:])
        zeroes += abs(delta) // 100
        delta = delta % (sign(delta) * 100)

        pointing = (pointing + delta) % 100
        true_delta = pointing - start_point
        
        if not pointing:
            zeroes += 1

        elif sign(true_delta) != sign(delta) and start_point != 0:
            zeroes += 1

    return zeroes

print(f"Part 1 solution: {part1()}")
print(f"Part 2 solution: {part2()}")