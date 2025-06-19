"""
Advent of code 2024 day 8
"""

# Part 1:
# Note that this is a copilot test

from collections import defaultdict

input_file = "inputs/day08.txt"

# Read input from file
with open(input_file) as f:
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


# Part 2:
# Note that this is a copilot test

from math import gcd

# Read input from file
with open(input_file) as f:
    grid = [line.rstrip("\n") for line in f]

height = len(grid)
width = len(grid[0]) if height > 0 else 0


def parse_antennas(grid):
    antennas = defaultdict(list)
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c.isalpha() or c.isdigit():
                antennas[c].append((x, y))
    return antennas


def mark_line(antinode_set, a, b, width, height):
    x1, y1 = a
    x2, y2 = b
    dx = x2 - x1
    dy = y2 - y1
    g = gcd(dx, dy)
    if g == 0:
        return
    dx //= g
    dy //= g

    # Find all points in bounds on this line
    # We'll scan through all possible t such that (x1 + t*dx, y1 + t*dy) is in bounds
    # Find min/max t so that x and y are in bounds
    t_min = max(
        (-(x1) // dx if dx != 0 else float("-inf")),
        (-(y1) // dy if dy != 0 else float("-inf")),
    )
    t_max = min(
        ((width - 1 - x1) // dx if dx != 0 else float("inf")),
        ((height - 1 - y1) // dy if dy != 0 else float("inf")),
    )
    # But let's just scan the whole grid for simplicity (it's not that big)
    for y in range(height):
        for x in range(width):
            # (x, y) is collinear with (x1, y1) and (x2, y2) if (x - x1, y - y1) is a multiple of (dx, dy)
            vx, vy = x - x1, y - y1
            if dx == 0:
                if vx == 0 and dy != 0 and vy % dy == 0:
                    antinode_set.add((x, y))
            elif dy == 0:
                if vy == 0 and dx != 0 and vx % dx == 0:
                    antinode_set.add((x, y))
            else:
                if vx * dy == vy * dx:
                    antinode_set.add((x, y))


def antinode_positions(grid, antennas):
    antinodes = set()
    for freq, positions in antennas.items():
        n = len(positions)
        if n < 2:
            continue
        for i in range(n):
            for j in range(i + 1, n):
                mark_line(antinodes, positions[i], positions[j], width, height)
    return antinodes


antennas = parse_antennas(grid)
antinodes = antinode_positions(grid, antennas)
print(f"The answer for Part 2 is: {len(antinodes)}")
