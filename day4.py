def search(r, c, rolls):
    roll_count = 0
    for i in range(r - 1, r + 2):
        for j in range(c - 1, c + 2):
            if i == r and j == c:
                pass
            elif i < 0 or i >= len(rolls):
                pass
            elif j < 0 or j >= len(rolls[i]):
                pass
            elif rolls[i][j] == "@":
                roll_count += 1
    return True if roll_count < 4 else False


if __name__ == "__main__":

    # part 1
    with open("data/day4.txt") as f:
        rolls = f.read().strip().split("\n")

    accessible = 0
    for i in range(len(rolls)):
        for j in range(len(rolls[0])):
            if rolls[i][j] == "@":
                if search(i, j, rolls):
                    accessible += 1

    print(accessible)
