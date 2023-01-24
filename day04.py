test = False


def read_input():
    global test
    filename = "inputs/day04-input.txt"
    if test:
        filename = "inputs/day04-test.txt"
    with open(filename, "r") as file:
        lines = []
        for line in file.readlines():
            e1, e2 = tuple(line.strip().split(","))
            e1min, e1max = tuple(map(int, e1.split("-")))
            e2min, e2max = tuple(map(int, e2.split("-")))
            lines.append((set(range(e1min, e1max + 1)), set(range(e2min, e2max + 1))))
        return lines


def main():
    lines = read_input()
    print(
        sum(
            [
                1 if ass1.issubset(ass2) or ass2.issubset(ass1) else 0
                for ass1, ass2 in lines
            ]
        )
    )
    print(sum([1 if ass1.intersection(ass2) else 0 for ass1, ass2 in lines]))


if __name__ == "__main__":
    main()
