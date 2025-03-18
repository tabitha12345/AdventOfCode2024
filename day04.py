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


# Look for two MAS or SAM that cross in the shape of an X:
def count_mas_and_sam_x(df):
    count_2 = 0
    rows, cols = df.shape

    # Check horizontally and vertically
    for r in range(rows):
        for c in range(cols - 3):
            if df.iloc[r, c : c + 4].tolist() == list("XMAS") or df.iloc[
                r, c : c + 4
            ].tolist() == list("SAMX"):
                count_2 += 1
            if df.iloc[c : c + 4, r].tolist() == list("XMAS") or df.iloc[
                c : c + 4, r
            ].tolist() == list("SAMX"):
                count_2 += 1

    # Check diagonally (top-left to bottom-right and top-right to bottom-left)
    for r in range(rows - 3):
        for c in range(cols - 3):
            if [df.iloc[r + i, c + i] for i in range(4)] == list("XMAS") or [
                df.iloc[r + i, c + i] for i in range(4)
            ] == list("SAMX"):
                count_2 += 1
            if [df.iloc[r + i, c + 3 - i] for i in range(4)] == list("XMAS") or [
                df.iloc[r + i, c + 3 - i] for i in range(4)
            ] == list("SAMX"):
                count_2 += 1


# Check for "MAS" or "SAM" crossing in the shape of an "X"
def count_mas_and_sam_x(df):
    count_2 = 0
    rows, cols = df.shape

    for r in range(rows - 2):
        for c in range(cols - 2):
            mas_diag1 = [df.iloc[r + i, c + i] for i in range(3)] == list("MAS")
            mas_diag2 = [df.iloc[r + i, c + 2 - i] for i in range(3)] == list("MAS")
            sam_diag1 = [df.iloc[r + i, c + i] for i in range(3)] == list("SAM")
            sam_diag2 = [df.iloc[r + i, c + 2 - i] for i in range(3)] == list("SAM")

            if (
                (mas_diag1 and mas_diag2)
                or (sam_diag1 and sam_diag2)
                or (mas_diag1 and sam_diag2)
                or (sam_diag1 and mas_diag2)
            ):
                count_2 += 1

    return count_2


xmas_count = count_xmas_and_samx(df)
x_count = count_mas_and_sam_x(df)

print(f"Part 1: The number of XMAS instances in any direction is: {xmas_count}")
print(f"Part 2: The number of XMAS instances in any direction is: {x_count}")
