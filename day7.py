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


if __name__ == "__main__":
    with open("data/day7.txt") as f:
        data = f.read().strip().split("\n")

    s = 0
    while data[0][s] == ".":
        s += 1

    MEMO = {}

    total_splits = descend(s, 0, data)
    print(total_splits)
