import numpy as np


def check_fake(id):
    id_len = len(id)
    if id_len % 2 != 0:
        return False
    else:
        lid = id[: int(id_len / 2)]
        rid = id[int(id_len / 2) :]

        if lid == rid:
            return True
        else:
            return False


def check_fake2(id):
    id_len = len(id)

    i = 1
    while i <= int(id_len / 2):

        if id_len % i == 0:
            subid = id[:i]
            if subid * int(id_len / i) == id:
                return True
            elif id_len % 2 != 0:
                return False
            else:
                i += 1
        else:
            i += 1

    return False


if __name__ == "__main__":
    with open("data/day2.txt") as f:
        id_ranges = f.read().strip().split(",")

    # part 1
    fake_sum = 0
    for id_range in id_ranges:
        start, end = id_range.split("-")
        for id in range(int(start), int(end) + 1):
            if check_fake(str(id)):
                fake_sum += id

    print(fake_sum)

    # part 2
    fake_sum2 = 0
    for id_range in id_ranges:
        start, end = id_range.split("-")
        for id in range(int(start), int(end) + 1):
            if check_fake2(str(id)):
                fake_sum2 += id

    print(fake_sum2)
