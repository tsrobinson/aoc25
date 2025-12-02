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


if __name__ == "__main__":
    with open("data/day2.txt") as f:
        lines = f.read().strip().split("\n")
