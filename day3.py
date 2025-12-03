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
