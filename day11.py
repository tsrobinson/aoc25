from collections import defaultdict, deque


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


if __name__ == "__main__":

    with open("data/day11.txt") as f:
        devices = f.read().splitlines()
        devices = {
            dev: paths.split() for dev, paths in (line.split(": ") for line in devices)
        }

    total_paths = conv_path("you")
    print(total_paths)

    # part 2
    # For part 2, we need paths from 'svr' to 'out' through both 'dac' and 'fft'
    # This equals: (paths svr->dac->fft->out) + (paths svr->fft->dac->out)

    # Build reverse graph to find all nodes that can reach a target

    def build_reverse_graph(devices):
        reverse = defaultdict(set)
        for node, neighbors in devices.items():
            for neighbor in neighbors:
                reverse[neighbor].add(node)
        return reverse

    def reachable_from(start, graph):
        """Find all nodes reachable from start using BFS"""
        visited = {start}
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return visited

    def reachable_to(end, reverse_graph):
        """Find all nodes that can reach end"""
        visited = {end}
        queue = deque([end])
        while queue:
            node = queue.popleft()
            for neighbor in reverse_graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return visited

    reverse_devices = build_reverse_graph(devices)

    # Nodes that can reach 'dac', 'fft', and 'out'
    reach_dac = reachable_to("dac", reverse_devices)
    reach_fft = reachable_to("fft", reverse_devices)
    reach_out = reachable_to("out", reverse_devices)

    # Nodes reachable from 'dac' and 'fft'
    from_dac = reachable_from("dac", devices)
    from_fft = reachable_from("fft", devices)

    # Count paths with memoization on filtered graph
    memo = {}

    def count_paths(start, end, must_visit):
        if (start, end, must_visit) in memo:
            return memo[(start, end, must_visit)]

        if start == end:
            return 1 if not must_visit else 0

        new_must = must_visit - {start}
        count = 0
        for neighbor in devices.get(start, []):
            count += count_paths(neighbor, end, new_must)

        memo[(start, end, must_visit)] = count
        return count

    # Paths through dac first, then fft
    paths1 = (
        count_paths("svr", "dac", frozenset())
        * count_paths("dac", "fft", frozenset())
        * count_paths("fft", "out", frozenset())
    )
    # Paths through fft first, then dac
    paths2 = (
        count_paths("svr", "fft", frozenset())
        * count_paths("fft", "dac", frozenset())
        * count_paths("dac", "out", frozenset())
    )

    total_paths_part2 = paths1 + paths2
    print(total_paths_part2)
