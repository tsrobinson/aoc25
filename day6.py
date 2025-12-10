if __name__ == "__main__":

    # part 1
    with open("data/day6.txt") as f:
        problems = f.read().strip().split("\n")
        problems = [line.split() for line in problems]

    solutions = []
    for i in range(len(problems[0])):
        op = problems[4][i]

        ans = int(problems[0][i])
        for j in range(1, 4):
            nxt = int(problems[j][i])
            if op == "+":
                ans += nxt
            elif op == "*":
                ans *= nxt

        solutions.append(ans)

    print(sum(solutions))

    # part 2
    with open("data/day6.txt") as f:
        problems = f.read().strip().split("\n")

    for i in range(len(problems[0])):
        ...
