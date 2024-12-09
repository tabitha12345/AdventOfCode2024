"""
Advent of code 2024 day 1
"""

from collections import Counter

# Set up the lists to be edited:
col1 = []
col2 = []
diff = []
frequency = {}
similarity_score = []

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

# For each item in col1 and col2, find the difference and add it to diff:
for item1, item2 in zip(col1, col2):
    difference = abs(int(item1) - int(item2))
    diff.append(difference)

# Add all the items in diff together:
total = sum(diff)

# Find the frequency of each item in col1 within col2:
col2_counter = Counter(col2)
for item in col1:
    frequency[item] = col2.count(item)

# Calculate the similarity score for each item:
for item in col1:
    score = int(item) * frequency[item]
    similarity_score.append(score)

# Add all the similarity scores together:
total_score = sum(similarity_score)

# Print the result:
print("Part 1: The total of the differences is " + str(total))
print("Part 2: The similarity score is " + str(total_score))
