test_input = False


def read_input():
    global test_input
    filename = "inputs/day14-input.txt"
    if test_input:
        filename = "inputs/day14-test.txt"
    with open(filename, "r") as file:
        return [
            list(map(lambda x: eval(x), line.strip().split(" -> ")))
            for line in file.readlines()
        ]


def simulate_sand(rock, deepest_rock, rock_bottom=False):
    reached_end = False
    not_air = set(rock)
    i = 0
    while not reached_end:
        grain = (500, 0)
        while True:
            check_below = (grain[0], grain[1] + 1)
            check_dl = (grain[0] - 1, grain[1] + 1)
            check_dr = (grain[0] + 1, grain[1] + 1)
            if rock_bottom:
                not_air.add((grain[0], deepest_rock + 2))
                not_air.add((grain[0] - 1, deepest_rock + 2))
                not_air.add((grain[0] + 1, deepest_rock + 2))
            elif check_below[1] > deepest_rock:
                reached_end = True
                break
            if check_below not in not_air:
                grain = check_below
                continue
            if check_dl not in not_air:
                grain = check_dl
                continue
            if check_dr not in not_air:
                grain = check_dr
                continue
            not_air.add(grain)
            break
        i += 1
        if grain == (500, 0):
            i += 1
            break
    print(i - 1)


def generate_rocks(paths):
    rock = set()
    deepest_rock = 0
    for path in paths:
        for i in range(len(path) - 1):
            start, end = path[i], path[i + 1]
            deepest_rock = max([deepest_rock, start[1], end[1]])
            if start[0] == end[0]:
                range_start = start[1]
                range_end = end[1]
                if start[1] > end[1]:
                    range_start = end[1]
                    range_end = start[1]
                for j in range(range_start, range_end + 1):
                    rock.add((start[0], j))
            else:
                range_start = start[0]
                range_end = end[0]
                if start[0] > end[0]:
                    range_start = end[0]
                    range_end = start[0]
                for j in range(range_start, range_end + 1):
                    rock.add((j, start[1]))
    return rock, deepest_rock


def main():
    rock, deepest_rock = generate_rocks(read_input())
    simulate_sand(rock, deepest_rock, False)
    simulate_sand(rock, deepest_rock, True)


if __name__ == "__main__":
    main()
