def in_range(range, item):
    lo, hi = [int(x) for x in range.split("-")]

    if item >= lo and item <= hi:
        return True
    else:
        return False


if __name__ == "__main__":

    # part 1
    with open("data/day5.txt") as f:
        ranges, items = f.read().strip().split("\n\n")
        ranges = ranges.split("\n")
        items = [int(x) for x in items.split("\n")]

    fresh = 0

    for item in items:
        for ran in ranges:
            if in_range(ran, item):
                fresh += 1
                break

    print(fresh)

    # part 2
    fresh = 0
    for ran in ranges:
        lo, hi = [int(x) for x in ran.split("-")]
