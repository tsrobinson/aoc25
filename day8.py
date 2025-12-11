from math import sqrt


def _euclid(x, y, z):
    return sqrt(x**2 + y**2 + z**2)


def _distance(a, b):
    x, y, z = [p1 - p2 for p1, p2 in zip(a, b)]
    return _euclid(x, y, z)


def _check_dict(i, j):

    if i == j:
        return True
    elif (i, j) in dist_matrix:
        return dist_matrix[(i, j)]
    elif (j, i) in dist_matrix:
        return dist_matrix[(j, i)]
    else:
        return False


if __name__ == "__main__":

    with open("data/day8.txt") as f:
        coords = f.read().strip().split("\n")

    coords = [[int(x) for x in a.split(",")] for a in coords]

    dist_matrix = {}
    for i in range(len(coords)):
        for j in range(len(coords)):
            if not _check_dict(i, j):
                dist_matrix[(i, j)] = _distance(coords[i], coords[j])

    connections = 0
    group = 0
    connect_dict = {}
    while connections < 1000:

        idx1, idx2 = min(dist_matrix, key=dist_matrix.get)
        del dist_matrix[(idx1, idx2)]

        if idx1 in connect_dict and idx2 in connect_dict:
            if connect_dict[idx1] != connect_dict[idx2]:
                c2 = connect_dict[idx2]
                connect_dict[idx2] = connect_dict[idx1]
                for k, v in connect_dict.items():
                    if v == c2:
                        connect_dict[k] = connect_dict[idx1]

        elif idx1 in connect_dict:
            connect_dict[idx2] = connect_dict[idx1]
        elif idx2 in connect_dict:
            connect_dict[idx1] = connect_dict[idx2]
        else:
            group += 1
            connect_dict[idx1] = group
            connect_dict[idx2] = group
        connections += 1

    group_dict = {}

    for k, v in connect_dict.items():
        if v not in group_dict:
            group_dict[v] = 1
        else:
            group_dict[v] += 1

    highest = sorted(group_dict.values(), reverse=True)[:3]

    out = highest[0] * highest[1] * highest[2]
