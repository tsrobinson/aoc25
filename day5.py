def in_range(range, item):
    lo, hi = [int(x) for x in range.split("-")]

    if item >= lo and item <= hi:
        return True
    else:
        return False


if __name__ == "__main__":

    # part 1
    with open("data/test5.txt") as f:
        ranges, items = f.read().strip().split("\n\n")
        ranges = ranges.split("\n")
        items = [int(x) for x in items.split("\n")]

    fresh = 0

    for item in items:
        for range in ranges:
            if in_range(range, item):
                fresh += 1
                break

    print(fresh)
