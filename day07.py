"""
Advent of code 2024 day 7
"""

# Part 1:

input_file = "inputs/day07.txt"


def can_make_target(numbers, target):
    def dfs(idx, current):
        if idx == len(numbers):
            return current == target
        # Try addition
        if dfs(idx + 1, current + numbers[idx]):
            return True
        # Try multiplication
        if dfs(idx + 1, current * numbers[idx]):
            return True
        return False

    return dfs(1, numbers[0])


input_file = "inputs/day07.txt"
total = 0

with open(input_file, "r") as file:
    for line in file:
        expected_total = int(line.split(":")[0])
        numbers_str = line.split(":")[1]
        numbers_list = [int(num) for num in numbers_str.strip().split()]
        if can_make_target(numbers_list, expected_total):
            total += expected_total

print("The total for Part 1 is " + str(total))
