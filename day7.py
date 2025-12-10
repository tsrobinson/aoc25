def descend(x, y, map):

    splits = 0

    if y == len(map) - 1:
        return splits
    elif map[y][x] in [".", "S"]:
        splits += descend(x, y + 1, map)
    elif map[y][x] == "^":
        if (x, y) not in MEMO:
            MEMO[(x, y)] = 1
            splits += 1
            splits += descend(x - 1, y + 1, map)
            splits += descend(x + 1, y + 1, map)

    return splits


def descend_quantum(x, y, grid):

    if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
        return 0

    # memoized result
    if (x, y) in MEMO:
        return MEMO[(x, y)]

    if y == len(grid) - 1:
        MEMO[(x, y)] = 1
        return 1

    cell = grid[y][x]

    if cell == "S" or cell == ".":
        # just move straight down
        worlds = descend_quantum(x, y + 1, grid)

    elif cell == "^":

        worlds = descend_quantum(x - 1, y + 1, grid)
        worlds += descend_quantum(x + 1, y + 1, grid)
    else:
        # unknown cell type => no paths
        worlds = 0

    MEMO[(x, y)] = worlds
    return worlds


if __name__ == "__main__":
    with open("data/day7.txt") as f:
        data = f.read().strip().split("\n")

    s = 0
    while data[0][s] == ".":
        s += 1

    # part 1
    MEMO = {}

    total_splits = descend(s, 0, data)
    print(total_splits)

    # part 2
    MEMO = {}
    worlds = descend_quantum(s, 0, data)
    print(worlds)
