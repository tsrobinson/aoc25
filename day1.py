import numpy as np
import pandas as pd


def rotate(start, dir, n):
    if dir == "R":
        return (start + n) % 100
    else:
        return (start - n) % 100


def rotate2(start, dir, n):
    if dir == "R":
        zero_clicks = (start + n) // 100
        newpos = (start + n) % 100
    else:
        if start == 0:
            start = 100
        zero_clicks = abs((start - n) // 100)
        newpos = (start - n) % 100
        if newpos == 0:
            zero_clicks += 1

    return (newpos, zero_clicks)


if __name__ == "__main__":
    with open("data/day1.txt") as f:
        lines = f.read().strip().split("\n")

    print("Part 1:")
    pos = 50
    pos_dict = {}
    for line in lines:
        dir = line[0]
        n = int(line[1:])
        pos = rotate(pos, dir, n)

        if pos in pos_dict:
            pos_dict[pos] += 1
        else:
            pos_dict[pos] = 1

    print(max(pos_dict.values()))

    print("Part 2:")
    pos = 50
    zero_clicks = 0
    for line in lines:
        dir = line[0]
        n = int(line[1:])
        pos, zc = rotate2(pos, dir, n)
        zero_clicks += zc
        print(dir, n, pos, zc)
    print(zero_clicks)
