"""
Advent of code 2024 day 10
"""

input_file = "inputs/day10.txt"


# Part 1:
# This is a copilot test


def read_map(filename):
    with open(filename) as f:
        return [list(map(int, line.strip())) for line in f if line.strip()]


def neighbors(x, y, width, height):
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < width and 0 <= ny < height:
            yield nx, ny


def find_trailhead_scores(heightmap):
    height = len(heightmap)
    width = len(heightmap[0])
    trailheads = [
        (x, y) for y in range(height) for x in range(width) if heightmap[y][x] == 0
    ]
    total_score = 0

    for tx, ty in trailheads:
        # BFS: (x, y, current_height)
        queue = [(tx, ty, 0)]
        visited = set()
        found_nines = set()
        while queue:
            x, y, h = queue.pop(0)
            if (x, y) in visited:
                continue
            visited.add((x, y))
            if heightmap[y][x] == 9:
                found_nines.add((x, y))
                continue
            for nx, ny in neighbors(x, y, width, height):
                nh = heightmap[ny][nx]
                if nh == h + 1:
                    queue.append((nx, ny, nh))
        total_score += len(found_nines)
    return total_score


# Part 2:
# this is a copilot test


from functools import lru_cache


def find_trailhead_ratings(heightmap):
    height = len(heightmap)
    width = len(heightmap[0])
    trailheads = [
        (x, y) for y in range(height) for x in range(width) if heightmap[y][x] == 0
    ]

    @lru_cache(maxsize=None)
    def dfs(x, y, h):
        if heightmap[y][x] == 9:
            return 1
        total = 0
        for nx, ny in neighbors(x, y, width, height):
            if heightmap[ny][nx] == h + 1:
                total += dfs(nx, ny, h + 1)
        return total

    total_rating = 0
    for tx, ty in trailheads:
        total_rating += dfs(tx, ty, 0)
    return total_rating


if __name__ == "__main__":
    heightmap = read_map(input_file)
    print("Part 1:", find_trailhead_scores(heightmap))
    print("Part 2:", find_trailhead_ratings(heightmap))
