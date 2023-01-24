import numpy as np

test = False


def read_input():
    global test
    filename = "inputs/day09-input.txt"
    if test:
        filename = "inputs/day09-test.txt"
    with open(filename, "r") as file:
        return list(map(lambda x: tuple(x.strip().split()), file.readlines()))


def move_head(head, direction):
    match direction:
        case "R":
            head[0] += 1
        case "L":
            head[0] -= 1
        case "U":
            head[1] += 1
        case "D":
            head[1] -= 1


def move_tail(head, tail):
    distance = np.linalg.norm(head - tail)
    if distance > np.sqrt(2):
        tail += np.sign(head - tail)


def move(knots, direction):
    move_head(knots[0], direction)
    head_tmp = knots[0]
    for tail in knots[1:]:
        move_tail(head_tmp, tail)
        head_tmp = tail


def simulate(size, moves):
    visited = set()
    knots = [np.zeros(2, dtype=int) for _ in range(size)]

    for direction, times in moves:
        times = int(times)
        for _ in range(times):
            move(knots, direction)
            visited.add(tuple(knots[-1]))

    print(len(visited))


def main():
    moves = read_input()
    simulate(2, moves)
    simulate(10, moves)


if __name__ == "__main__":
    main()
