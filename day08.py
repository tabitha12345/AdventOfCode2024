"""
Advent of code 2024 day 8
"""

# Note that this is a copilot test

from collections import defaultdict

# Read input from file
with open("inputs/day08.txt") as f:
    grid = [line.rstrip("\n") for line in f]

freq_positions = defaultdict(list)
for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c != ".":
            freq_positions[c].append((x, y))

antinodes = set()
height = len(grid)
width = len(grid[0])

for freq, positions in freq_positions.items():
    n = len(positions)
    for i in range(n):
        x1, y1 = positions[i]
        for j in range(n):
            if i == j:
                continue
            x2, y2 = positions[j]
            # Calculate antinode position: 2*x2 - x1, 2*y2 - y1
            ax = 2 * x2 - x1
            ay = 2 * y2 - y1
            if 0 <= ax < width and 0 <= ay < height:
                antinodes.add((ax, ay))

print("The answer for Part 1 is: " + str(len(antinodes)))
