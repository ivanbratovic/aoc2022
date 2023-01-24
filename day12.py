import numpy as np

test_input = False
dead_nodes = set()


def read_input():
    global test_input
    filename = "inputs/day12-input.txt"
    if test_input:
        filename = "inputs/day12-test.txt"
    with open(filename, "r") as file:
        return np.array(
            list(
                map(
                    lambda x: list([ord(char) - 97 for char in x.strip()]),
                    file.readlines(),
                )
            )
        )


def manhattan_dist(a, b):
    return np.abs(a[0] - b[0]) + np.abs(a[1] - b[1])


def expand_node(graph, node):
    valid_neighbours = []
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if abs(dx) == abs(dy):
                continue
            x, y = node[0] + dx, node[1] + dy
            if x < 0 or y < 0:
                continue
            if x >= graph.shape[0] or y >= graph.shape[1]:
                continue
            if graph[node] - graph[(x, y)] < -1:  # Cannot climb, but can drop down
                continue
            valid_neighbours.append((x, y))
    return valid_neighbours


def a_star(graph, start, end):
    global dead_nodes
    opened = []
    came_from = {}
    costs = {}

    opened.append((start, manhattan_dist(start, end)))
    came_from[start] = None
    costs[start] = 0

    while len(opened):
        opened = sorted(opened, key=lambda x: x[1], reverse=True)
        current, _ = opened.pop()
        if current in dead_nodes:
            continue

        if current == end:
            break

        for next_node in expand_node(graph, current):
            if next_node in dead_nodes:
                continue
            cost = costs[current] + 1
            if next_node not in costs or cost < costs[next_node]:
                costs[next_node] = cost
                came_from[next_node] = current
                opened.append((next_node, cost + manhattan_dist(next_node, end)))
    else:
        if start not in dead_nodes:
            for node in costs.keys():
                dead_nodes.add(node)

    return came_from


def count_steps(graph, start, end):
    came_from = a_star(graph, start, end)

    if end not in came_from:
        return graph.shape[0] * graph.shape[1]
    current = came_from[end]
    path = [end]
    while current:
        current = came_from[current]
        path.append(current)
    return len(path) - 1


def main():
    height_map = read_input()
    start = tuple(map(int, np.where(height_map == -14)))
    end = tuple(map(int, np.where(height_map == -28)))
    height_map[start] = ord("a") - 97
    height_map[end] = ord("z") - 97

    print(count_steps(height_map, start, end))
    print(
        min(
            [
                count_steps(height_map, start, end)
                for start in zip(*np.where(height_map == ord("a") - 97))
            ]
        )
    )


if __name__ == "__main__":
    main()
