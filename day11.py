def conv_path(path, end="out"):
    npaths = 0
    nxt_devs = devices[path]
    if devices[path] == [end]:
        return 1
    elif devices[path] == ["out"]:
        return 0
    else:
        for dev in nxt_devs:
            npaths += conv_path(dev, end)
    return npaths


PART2_MEMO = {}


def conv_path2(path, vdac=0, vfft=0):
    if path == "dac":
        vdac = 1
    elif path == "fft":
        vfft = 1

    if (path, vdac, vfft) in PART2_MEMO:
        return PART2_MEMO[(path, vdac, vfft)]

    nxt_devs = devices[path]

    if devices[path] == ["out"]:
        npaths = vdac * vfft
    else:
        npaths = 0
        for dev in nxt_devs:
            npaths += conv_path2(dev, vdac, vfft)
    PART2_MEMO[(path, vdac, vfft)] = npaths
    return npaths


if __name__ == "__main__":

    with open("data/day11.txt") as f:
        devices = f.read().splitlines()
        devices = {
            dev: paths.split() for dev, paths in (line.split(": ") for line in devices)
        }

    total_paths = conv_path("you")
    print(total_paths)

    # part 2
    total_valid_paths = conv_path2("svr")
    print(total_valid_paths)
