import re

test_input = False


def read_input():
    filename = "inputs/day21-input.txt"
    if test_input:
        filename = "inputs/day21-test.txt"
    with open(filename, "r") as file:
        return {k: v for k, v in map(lambda l: l.strip().split(": "), file.readlines())}


def figure_out_root(monkeys):
    literals = {}

    while len(literals) != len(monkeys):
        for key in monkeys:
            if key in literals:
                continue
            try:
                val = int(monkeys[key])
                literals[key] = val
            except ValueError:
                try:
                    val = eval(f"{monkeys[key]}", dict(literals))
                    literals[key] = val
                except NameError:
                    continue
    return literals["root"]


def figure_out_humn(monkeys, start=0, step_factor=0.02):
    # Solve for root=0
    monkeys["root"] = re.sub(r" . ", " - ", monkeys["root"])
    humn = 1

    while True:
        monkeys["humn"] = str(humn)
        root = figure_out_root(monkeys)
        if root == 0:
            return humn
        step = int(root * step_factor)
        if step == 0:
            step = int(root * step_factor / abs(root * step_factor))
        humn += step


def main():
    monkeys = read_input()
    print(int(figure_out_root(monkeys)))
    print(figure_out_humn(monkeys, start=3, step_factor=0.03))


if __name__ == "__main__":
    main()
