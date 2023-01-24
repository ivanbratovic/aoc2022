test_input = False


def read_input():
    global test_input
    filename = "inputs/day13-input.txt"
    if test_input:
        filename = "inputs/day13-test.txt"
    with open(filename, "r") as file:
        return [eval(line.strip()) for line in file.readlines() if line != "\n"]


def compare(left, right):
    if type(left) != type(right):
        if type(left) == int:
            return compare([left], right)
        return compare(left, [right])
    if type(left) == int:
        if left < right:
            return True
        if left > right:
            return False
        return None
    for value_left, value_right in zip(left, right):
        if (result := compare(value_left, value_right)) is not None:
            return result
    if len(left) < len(right):
        return True
    if len(left) > len(right):
        return False
    return None


def main():
    signals = read_input()
    print(
        sum(
            [
                i // 2 + 1
                for i in range(0, len(signals), 2)
                if compare(signals[i], signals[i + 1])
            ]
        )
    )

    divider_1 = [[2]]
    divider_2 = [[6]]
    signals.append(divider_1)
    signals.append(divider_2)
    mijenjao = True
    while mijenjao:
        mijenjao = False
        for i in range(len(signals) - 1):
            if not compare(signals[i], signals[i + 1]):
                signals[i], signals[i + 1] = signals[i + 1], signals[i]
                mijenjao = True
    print((signals.index(divider_1) + 1) * (signals.index(divider_2) + 1))


if __name__ == "__main__":
    main()
