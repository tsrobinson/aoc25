if __name__ == "__main__":

    with open("data/day9.txt") as f:
        tiles = [a.split(",") for a in f.read().splitlines()]

    areas = []
    visited = set()

    for i in range(len(tiles)):
        for j in range(len(tiles)):
            if i == j:
                continue
            if (i, j) in visited or (j, i) in visited:
                continue
            else:
                visited.add((i, j))
                area_ij = (1 + abs(int(tiles[i][0]) - int(tiles[j][0]))) * (
                    1 + abs(int(tiles[i][1]) - int(tiles[j][1]))
                )
                areas.append(area_ij)

    print(max(areas))

    # part 2
    dim_x = max(int(a[0]) for a in tiles) + 1
    dim_y = max(int(a[1]) for a in tiles) + 1
