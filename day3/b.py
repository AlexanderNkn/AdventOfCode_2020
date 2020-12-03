def reader():
    with open('day3/puzzle_input.txt', 'r') as f:
        return f.read().splitlines()


def tree(right, down):
    count = 0
    index = 0
    lines = reader()
    for i in range(0, len(lines), down):
        line = lines[i]
        if line[index] == '#':
            count += 1
        remainder = len(line) - index - 1
        index = (
            index + right if remainder > right - 1 else right - 1 - remainder
        )
    return count


multiply = 1
for right, down in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
    multiply *= tree(right, down)

print(multiply)
