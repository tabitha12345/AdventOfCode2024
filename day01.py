"""
Advent of code 2024 day 1, part 1
"""

# Set up the lists to be edited:
col1 = []
col2 = []
diff = []


# Add each entry in each of the columns to a list:
with open("inputs/day01.txt", "r") as file:
    for line in file:
        entry1 = line.split("   ")[0].strip()
        entry2 = line.split("   ")[1].strip()
        col1.append(entry1)
        col2.append(entry2)

# Sort each list:
col1.sort()
col2.sort()

print(col1)
print(col2)

# For each item in col1 and col2, find the difference and add it to diff:
for item1, item2 in zip(col1, col2):
    difference = abs(int(item1) - int(item2))
    diff.append(difference)

# Add all the items in diff together:
total = sum(diff)

# Print the result:
print(str(total))
