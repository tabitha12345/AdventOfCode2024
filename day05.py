"""
Advent of code 2024 day 5
"""

from collections import defaultdict, deque

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


def part1():
    rules, updates = parse_input(input_file)
    rule_pairs = parse_rules(rules)
    updates = parse_updates(updates)
    total = 0
    for update in updates:
        if is_update_valid(update, rule_pairs):
            total += middle_value(update)
    print("The answer for Part 1 is: " + str(total))


part1()

# Part 2:


def topological_sort(pages, rule_pairs):
    adj = defaultdict(list)
    indegree = defaultdict(int)
    page_set = set(pages)
    for x, y in rule_pairs:
        if x in page_set and y in page_set:
            adj[x].append(y)
            indegree[y] += 1
            indegree.setdefault(x, 0)
    order = {p: i for i, p in enumerate(pages)}
    queue = deque([p for p in pages if indegree[p] == 0])
    result = []
    while queue:
        queue = deque(sorted(queue, key=lambda x: order[x]))
        node = queue.popleft()
        result.append(node)
        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    if len(result) != len(pages):
        raise ValueError("Cycle detected or missing pages in topological sort")
    return result


def part2():
    rules, updates = parse_input(input_file)
    rule_pairs = parse_rules(rules)
    updates = parse_updates(updates)
    total = 0
    for update in updates:
        if not is_update_valid(update, rule_pairs):
            sorted_update = topological_sort(update, rule_pairs)
            total += middle_value(sorted_update)
    print("The answer for Part 2 is: " + str(total))


part2()
