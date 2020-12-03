# For example, suppose you have the following list:
# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc
# Each line gives the password policy and then the password. The password
# policy indicates the lowest and highest number of times a given letter must
# appear for the password to be valid. For example, 1-3 a means that the
# password must contain a at least 1 time and at most 3 times.
# In the above example, 2 passwords are valid. The middle password, cdefg, is
# not; it contains no instances of b, but needs at least 1. The first and third
# passwords are valid: they contain one a or nine c, both within the limits of
# their respective policies.
# How many passwords are valid according to their policies?

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
    if int(item[0]) <= item[3].count(item[2]) <= int(item[1]):
        count += 1

print(count)
