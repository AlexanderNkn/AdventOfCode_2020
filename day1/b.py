# The Elves in accounting are thankful for your help; one of them even offers
# you a starfish coin they had left over from a past vacation. They offer you a
# second one if you can find three numbers in your expense report that meet the
# same criteria.
# Using the above example again, the three entries that sum to 2020 are 979,
# 366, and 675. Multiplying them together produces the answer, 241861950.
# In your expense report, what is the product of the three entries
# that sum to 2020?

with open('day1/puzzle_input.txt', 'r') as f:
    puzzle = list(map(int, f.read().split()))
puzzle.sort()
lt = 0
mid = 1
rt = len(puzzle) - 1
while True:
    if puzzle[lt] + puzzle[mid] + puzzle[rt] > 2020:
        rt -= 1
    elif puzzle[lt] + puzzle[mid] + puzzle[rt] < 2020:
        mid = lt + 1
        while puzzle[lt] + puzzle[mid] + puzzle[rt] < 2020 and mid + 1 < rt:
            mid += 1
            if puzzle[lt] + puzzle[mid] + puzzle[rt] == 2020:
                break
        lt += 1
        mid += 1
    else:
        break

print(puzzle[lt] * puzzle[mid] * puzzle[rt])
