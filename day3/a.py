def reader():
    with open('day3/puzzle_input.txt', 'r') as f:
        for line in f:
            yield line.rstrip('\n')


index = 0
count = 0
for line in reader():
    if line[index] == '#':
        count += 1
    remainder = len(line) - index - 1
    index = index + 3 if remainder > 2 else 2 - remainder

print(count)
