"""
Advent of code 2023 day 1
"""

# Set up the lists to be edited:
col1 = []
col2 = []

# Add each entry in each of the columns to a list:
with open("inputs/day01.txt", "r") as file:
    for line in file:
        entry1 = line.split("   ")[0].strip()
        entry2 = line.split("   ")[1].strip()
        col1.append(entry1)
        col2.append(entry2)
