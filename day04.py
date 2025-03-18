"""
Advent of code 2024 day 4
"""

import pandas as pd

input_file = "inputs/day04.txt"


grid = []

# Put contents of text file into a dataframe:
with open(input_file) as file:
    for line in file:
        grid.append(list(line.rstrip("\n")))

df = pd.DataFrame(grid)


# Look for XMAS or SAMX in any direction:
def count_xmas_and_samx(df):
    count = 0
    rows, cols = df.shape

    # Check horizontally and vertically
    for r in range(rows):
        for c in range(cols - 3):
            if df.iloc[r, c : c + 4].tolist() == list("XMAS") or df.iloc[
                r, c : c + 4
            ].tolist() == list("SAMX"):
                count += 1
            if df.iloc[c : c + 4, r].tolist() == list("XMAS") or df.iloc[
                c : c + 4, r
            ].tolist() == list("SAMX"):
                count += 1

    # Check diagonally (top-left to bottom-right and top-right to bottom-left)
    for r in range(rows - 3):
        for c in range(cols - 3):
            if [df.iloc[r + i, c + i] for i in range(4)] == list("XMAS") or [
                df.iloc[r + i, c + i] for i in range(4)
            ] == list("SAMX"):
                count += 1
            if [df.iloc[r + i, c + 3 - i] for i in range(4)] == list("XMAS") or [
                df.iloc[r + i, c + 3 - i] for i in range(4)
            ] == list("SAMX"):
                count += 1

    return count


xmas_count = count_xmas_and_samx(df)
print(f"Part 1: The number of XMAS instances in any direction is: {xmas_count}")
