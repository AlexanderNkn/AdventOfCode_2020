# Each policy actually describes two positions in the password, where 1 means
# the first character, 2 means the second character, and so on. (Be careful;
# Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of
# these positions must contain the given letter. Other occurrences of the
# letter are irrelevant for the purposes of policy enforcement.
# Given the same example list from above:
# 1-3 a: abcde is valid: position 1 contains a and position 3 does not.
# 1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
# 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
# How many passwords are valid according to the new interpretation of the
# policies?

with open('day2/puzzle_input.txt', 'r') as f:
    lines = f.readlines()

result = []
for line in lines:
    item = line.split()
    min_occurence = item[0].split('-')[0]
    max_occurence = item[0].split('-')[1]
    letter = item[1][0]
    string = item[2]
    result.append((min_occurence, max_occurence, letter, string))

count = 0
for item in result:
    min_position = int(item[0]) - 1
    max_position = int(item[1]) - 1
    letter = item[2]
    string = item[3]
    if (string[min_position] == letter) != (string[max_position] == letter):
        count += 1

print(count)
