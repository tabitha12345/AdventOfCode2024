"""
Advent of code 2024 day 6
"""

# Part 1:

input_file = "inputs/day06.txt"

# load each line of the text file into a list
with open(input_file, "r") as f:
    grid = [list(line) for line in f]


def find_guard(grid):
    # find the location and direction the guard is facing
    arrows = {"^", ">", "<", "v"}
    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            if cell in arrows:
                return (row_idx, col_idx, cell)
    return None


position = find_guard(grid)
print("The starting position of the guard is " + str(position))

while True:
    # move the guard in the current direction if it's not blocked
    rows, cols = len(grid), len(grid[0])
    row, col = position[0], position[1]
    if position[2] == "^":
        # if direction is UP
        if row - 1 >= 0 and grid[row - 1][col] != "#":
            grid[row][col] = "x"  # Replace current ^ with x
            grid[row - 1][col] = "^"  # Move ^ up one row
            position = (row - 1, col, "^")  # Update position
        elif row - 1 < 0:
            grid[row][col] = "x"  # Replace current ^ with x
            print("guard has left the matrix")
            break
        else:
            grid[row][col] = ">"  # turn right
            position = (row, col, ">")
    elif position[2] == ">":
        # if direction is RIGHT
        if col + 1 < cols and grid[row][col + 1] != "#":
            grid[row][col] = "x"  # Replace current > with x
            grid[row][col + 1] = ">"  # Move > right by one
            position = (row, col + 1, ">")  # Update position
        elif col + 1 >= cols:
            grid[row][col] = "x"  # Replace current > with x
            print("guard has left the matrix")
            break
        else:
            grid[row][col] = "v"  # turn right
            position = (row, col, "v")
    elif position[2] == "v":
        # if direction is DOWN
        if row + 1 < rows and grid[row + 1][col] != "#":
            grid[row][col] = "x"  # Replace current v with x
            grid[row + 1][col] = "v"  # Move v down one row
            position = (row + 1, col, "v")  # Update position
        elif row + 1 >= rows:
            grid[row][col] = "x"  # Replace current v with x
            print("guard has left the matrix")
            break
        else:
            grid[row][col] = "<"  # turn right
            position = (row, col, "<")
    elif position[2] == "<":
        # if direction is LEFT
        if col - 1 >= 0 and grid[row][col - 1] != "#":
            grid[row][col] = "x"  # Replace current v with x
            grid[row][col - 1] = "<"
            position = (row, col - 1, "<")
        elif col - 1 < 0:
            grid[row][col] = "x"  # Replace current < with x
            print("guard has left the matrix")
            break
        else:
            grid[row][col] = "^"  # turn right
            position = (row, col, "^")

position = find_guard(grid)
print("The ending position of the guard is " + str(position))

visited_locations = sum(row.count("x") for row in grid)
print(f"Part 1: Number of locations visited by the guard: {visited_locations}")


# Part 2:
# Note: This is a copilot test

import copy


def load_grid(filename):
    with open(filename, "r") as f:
        return [list(line.rstrip("\n")) for line in f]


def find_guard(grid):
    arrows = {"^", ">", "<", "v"}
    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            if cell in arrows:
                return (row_idx, col_idx, cell)
    return None


def simulate_with_obstacle(grid, obstacle_pos, start_pos):
    grid = copy.deepcopy(grid)
    grid[obstacle_pos[0]][obstacle_pos[1]] = "#"
    position = start_pos
    rows, cols = len(grid), len(grid[0])
    visited_states = set()
    while True:
        state = (position[0], position[1], position[2])
        if state in visited_states:
            # Loop detected
            return True
        visited_states.add(state)
        row, col, direction = position
        if direction == "^":
            if row - 1 >= 0 and grid[row - 1][col] != "#":
                position = (row - 1, col, "^")
            elif row - 1 < 0:
                break
            else:
                position = (row, col, ">")
        elif direction == ">":
            if col + 1 < cols and grid[row][col + 1] != "#":
                position = (row, col + 1, ">")
            elif col + 1 >= cols:
                break
            else:
                position = (row, col, "v")
        elif direction == "v":
            if row + 1 < rows and grid[row + 1][col] != "#":
                position = (row + 1, col, "v")
            elif row + 1 >= rows:
                break
            else:
                position = (row, col, "<")
        elif direction == "<":
            if col - 1 >= 0 and grid[row][col - 1] != "#":
                position = (row, col - 1, "<")
            elif col - 1 < 0:
                break
            else:
                position = (row, col, "^")
    return False


def part2(grid):
    start_pos = find_guard(grid)
    rows, cols = len(grid), len(grid[0])
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "#" or (r, c) == (start_pos[0], start_pos[1]):
                continue
            if grid[r][c] in {".", "x"}:
                if simulate_with_obstacle(grid, (r, c), start_pos):
                    count += 1
    print(f"Part 2: Number of positions that cause a loop: {count}")


grid = load_grid(input_file)
part2(grid)
