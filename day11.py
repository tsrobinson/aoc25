def conv_path(path):

    npaths = 0
    nxt_devs = devices[path]

    if devices[path] == ["out"]:
        return 1
    else:
        for dev in nxt_devs:
            npaths += conv_path(dev)

    return npaths


if __name__ == "__main__":

    with open("data/day11.txt") as f:
        devices = f.read().splitlines()
        devices = {
            dev: paths.split() for dev, paths in (line.split(": ") for line in devices)
        }

    total_paths = conv_path("you")
    print(total_paths)
