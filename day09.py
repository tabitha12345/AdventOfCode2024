"""
Advent of code 2024 day 9
"""

input_file = "inputs/day09.txt"


# Part 1:


# Read the disk map from the input file and parse it into a list of integers.
def parse_disk_map(input_file):
    with open(input_file, "r") as file:
        disk_map = file.read().strip()
    return [int(digit) for digit in disk_map]


# Translate the list of integers into a list of ids and "spaces".
def disk_map_to_ids_and_spaces(lengths):
    result = []
    file_id = 0
    is_file = True
    for length in lengths:
        if is_file:
            result.extend([file_id] * length)
            file_id += 1
        else:
            result.extend(["."] * length)
        is_file = not is_file
    return result


# Move the integer one at a time from the right hand side to the far most left "space".
def compact_disk(ids_and_spaces):
    ids_and_spaces = ids_and_spaces.copy()
    while True:
        # Find the rightmost file block
        right = len(ids_and_spaces) - 1
        while right >= 0 and ids_and_spaces[right] == ".":
            right -= 1
        if right < 0:
            break  # No more file blocks

        # Find the leftmost space
        left = 0
        while left < len(ids_and_spaces) and ids_and_spaces[left] != ".":
            left += 1
        if left >= right:
            break  # No more moves possible

        # Move the rightmost file block to the leftmost space
        ids_and_spaces[left] = ids_and_spaces[right]
        ids_and_spaces[right] = "."

    return ids_and_spaces


# Calculate the checksum.
def calculate_checksum(compacted):
    checksum = 0
    for pos, val in enumerate(compacted):
        if val != ".":
            checksum += pos * int(val)
    return checksum


lengths = parse_disk_map(input_file)
ids_and_spaces = disk_map_to_ids_and_spaces(lengths)
compacted = compact_disk(ids_and_spaces)
print("Part 1: Checksum:", calculate_checksum(compacted))

# Part 2:


def compact_disk_whole_files(ids_and_spaces):
    ids_and_spaces = ids_and_spaces.copy()
    # Find all file IDs (integers, not ".")
    file_ids = sorted({x for x in ids_and_spaces if x != "."}, reverse=True)
    for file_id in file_ids:
        # Find all blocks for this file
        indices = [i for i, x in enumerate(ids_and_spaces) if x == file_id]
        if not indices:
            continue
        file_len = len(indices)
        file_start = indices[0]
        file_end = indices[-1]
        # Search for leftmost span of free spaces before file_start
        left = 0
        while left + file_len <= file_start:
            if all(ids_and_spaces[i] == "." for i in range(left, left + file_len)):
                # Move file to this span
                for i in indices:
                    ids_and_spaces[i] = "."
                for i in range(left, left + file_len):
                    ids_and_spaces[i] = file_id
                break
            left += 1
    return ids_and_spaces


lengths = parse_disk_map(input_file)
ids_and_spaces = disk_map_to_ids_and_spaces(lengths)
compacted2 = compact_disk_whole_files(ids_and_spaces)
print("Part 2: Checksum:", calculate_checksum(compacted2))
