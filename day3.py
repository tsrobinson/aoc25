if __name__ == "__main__":

    with open("data/day3.txt") as f:
        banks = f.read().strip().split("\n")

    # part 1
    total_joltage = 0
    for bank in banks:
        joltage = bank[:2]
        for i in range(1, len(bank)):
            if i == len(bank) - 1:
                if int(bank[i]) > int(joltage[1]):
                    joltage = joltage[0] + bank[i]
            elif int(bank[i]) > int(joltage[0]):
                joltage = bank[i : i + 2]
            elif int(bank[i]) > int(joltage[1]):
                joltage = joltage[0] + bank[i]
        total_joltage += int(joltage)

    # part 1 (better)
    total_joltage = 0
    for bank in banks:
        bank = [int(b) for b in bank]
        joltage = [0, 0]
        l = 0
        for i in range(len(bank) - 1):
            if bank[i] > joltage[0]:
                joltage[0] = bank[i]
                l = i

        for i in range(l + 1, len(bank)):
            if bank[i] > joltage[1]:
                joltage[1] = bank[i]

        total_joltage += int("".join([str(x) for x in joltage]))

    # part 2
    total_joltage = 0
    for bank in banks:
        bank = [int(b) for b in bank]
        joltage = [0] * 12
        start = -1
        for s in range(12):
            end = len(bank) - 11 + s
            for i in range(start + 1, end):
                if bank[i] > joltage[s]:
                    joltage[s] = bank[i]
                    start = i

        total_joltage += int("".join([str(x) for x in joltage]))
