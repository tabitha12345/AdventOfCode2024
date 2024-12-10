"""
Advent of code 2024 day 2
"""

counter_part_1 = 0
counter_part_2 = 0


def is_decreasing(levels):
    # Determine if the levels are decreasing by 1-3:
    for i in range(1, len(levels)):
        if not (1 <= levels[i - 1] - levels[i] <= 3):
            return False
    return True


def is_increasing(levels):
    # Determine if the levels are increasing by 1-3:
    for i in range(1, len(levels)):
        if not (1 <= levels[i] - levels[i - 1] <= 3):
            return False
    return True


def using_problem_dampener(levels):
    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i + 1 :]
        if is_decreasing(new_levels) or is_increasing(new_levels):
            return True
    return False


with open("inputs/day02.txt", "r") as file:
    for report in file:
        levels = list(map(int, report.strip().split()))
        if is_decreasing(levels) or is_increasing(levels):
            # Add to counter for every report that is already safe with basic rules:
            counter_part_1 += 1
            counter_part_2 += 1
        elif using_problem_dampener(levels):
            # Add to counter for every report that is safe if using problem dampener:
            counter_part_2 += 1

print("Part 1: The number of safe reports is " + str(counter_part_1))
print("Part 1: The number of safe reports is " + str(counter_part_2))
