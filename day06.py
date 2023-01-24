test = False


def read_input():
    global test
    filename = "inputs/day06-input.txt"
    if test:
        filename = "inputs/day06-test.txt"
    with open(filename, "r") as file:
        return file.readline().strip()


def marker(signal, marker_len):
    return [
        len(set(signal[i - marker_len : i])) == marker_len
        for i in range(marker_len, len(signal))
    ].index(True) + marker_len


def main():
    signal = read_input()
    print(marker(signal, 4))
    print(marker(signal, 14))


if __name__ == "__main__":
    main()
