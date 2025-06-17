"""
Advent of code 2024 day 5
"""

input_file = "inputs/day05.txt"

# Part 1:

def parse_input(filename):
    with open(filename) as f:
        lines = [line.strip() for line in f if line.strip()]
    # Find split between rules and updates
    split_idx = 0
    for i, line in enumerate(lines):
        if "," in line:
            split_idx = i
            break
    rules = lines[:split_idx]
    updates = lines[split_idx:]
    return rules, updates


def parse_rules(rules):
    rule_pairs = []
    for rule in rules:
        x, y = map(int, rule.split("|"))
        rule_pairs.append((x, y))
    return rule_pairs


def parse_updates(updates):
    return [list(map(int, line.split(","))) for line in updates]


def is_update_valid(update, rule_pairs):
    pos = {page: i for i, page in enumerate(update)}
    for x, y in rule_pairs:
        if x in pos and y in pos:
            if pos[x] >= pos[y]:
                return False
    return True


def middle_value(update):
    n = len(update)
    return update[n // 2]


def main():
    rules, updates = parse_input(input_file)
    rule_pairs = parse_rules(rules)
    updates = parse_updates(updates)
    total = 0
    for update in updates:
        if is_update_valid(update, rule_pairs):
            total += middle_value(update)
    print("The answer for Part 1 is: " + str(total))


main()
