import numpy as np

test = False

def read_input():
    global test
    filename = "inputs/day10-input.txt"
    if test:
        filename = "inputs/day10-test.txt"
    with open(filename, "r") as file:
        return list(map(lambda x: tuple(x.strip().split()), file.readlines()))

def run(program):
    sums = 0
    regX = 1
    cycle = 0
    adding = 0
    while True:
        cycle += 1
        # Before the cycle
        if adding:
            add_at_end = True
        else:
            add_at_end = False
            try:
                cmd = program.pop()
            except IndexError:
                break
            match cmd:
                case ["noop"]:
                    adding = 0
                case ["addx", x]:
                    adding = int(x)
        # During the cycle
        current_pixel = (cycle - 1) % 40
        if abs(current_pixel - regX) < 2:
            print("█", end="")
        else:
            print(" ", end="")
        if current_pixel == 39:
            print()
        if cycle in (20, 60, 100, 140, 180, 220):
            sums += cycle * regX
        # After the cycle
        if add_at_end:
            regX += adding
            adding = 0
    print("Part 1:", sums)

        

def main():
    program = read_input()
    run(program[::-1])



if __name__ == "__main__":
    main()