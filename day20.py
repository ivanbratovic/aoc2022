test_input = False

def read_input():
    filename = "inputs/day20-input.txt"
    if test_input:
        filename = "inputs/day20-test.txt"
    with open(filename, "r") as file:
        return [(int(el), i) for i, el in enumerate(file.readlines())]

def mix(l, repeat=1):
    init = list(l)
    zero = None
    for _ in range(repeat):
        for el in init:
            if el[0] == 0:
                zero = el
            idx = l.index(el)
            l.pop(idx)
            new_idx = (el[0] + idx) % len(l)
            l.insert(new_idx, el)
    
    return l, zero

def calc_coordinates(repeat=1, mult=1):
    l, zero = mix([(el * mult, i) for el, i in read_input()], repeat)
    zero_idx = l.index(zero)
    print(sum([l[(zero_idx + X) % len(l)][0] for X in [1000, 2000, 3000]]))

def main():
    calc_coordinates()
    calc_coordinates(repeat=10, mult=811589153)


if __name__ == "__main__":
    main()