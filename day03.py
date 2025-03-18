"""
Advent of code 2024 day 3
"""

import re

input_file = "inputs/day03.txt"
total_sum = 0
total_sum_2 = 0


def find_and_multiply(input_file):
    with open(input_file, "r") as file:
        input_data = file.read()

    # Find mul(X,Y) where X and Y are numbers
    pattern = re.compile(r"mul\((\d+),(\d+)\)")
    matches = pattern.findall(input_data)

    total_sum = 0
    for match in matches:
        x, y = map(int, match)
        total_sum += x * y

    return total_sum


def find_and_multiply_conditional(input_file):
    with open(input_file, "r") as file:
        input_data = file.read()

    # Find mul(X,Y) where X and Y are numbers
    pattern_conditional = re.compile(r"(mul\((\d+),(\d+)\))|(do\(\))|(don't\(\))")
    matches_conditional = pattern_conditional.findall(input_data)

    total_sum_2 = 0
    mul_enabled = True

    for match in matches_conditional:
        if match[1] and match[2]:
            if mul_enabled:
                x, y = int(match[1]), int(match[2])
                total_sum_2 += x * y
        elif match[3]:  # do() match
            mul_enabled = True
        elif match[4]:  # don't() match
            mul_enabled = False

    return total_sum_2


result1 = find_and_multiply(input_file)
print(f"Part 1: The sum of all valid multiplications is: {result1}")

result2 = find_and_multiply_conditional(input_file)
print(f"Part 2: The sum of all valid multiplications is: {result2}")
