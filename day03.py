"""
Advent of code 2024 day 3
"""

import re

input_file = "inputs/day03.txt"
total_sum = 0


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


result1 = find_and_multiply(input_file)
print(f"Part 1: The sum of all valid multiplications is: {result1}")
