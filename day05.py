from dataclasses import dataclass
from copy import deepcopy
import re


test = False


def read_input():
    global test
    filename = "inputs/day05-input.txt"
    if test:
        filename = "inputs/day05-test.txt"
    with open(filename, "r") as file:
        crates = []
        moves = []
        adding_moves = False
        for line in map(lambda x: x.strip("\n"), file.readlines()):
            if line == "":
                adding_moves = True
                continue
            if adding_moves:
                moves.append(tuple(map(int, re.findall(r"\d+", line))))
            else:
                line = re.sub(" {4}", " [ ]", line)
                line = re.sub(r"^ \[ \]", "[ ] ", line)
                crates.append(tuple(re.findall(r"\[(.)\]", line)))
        return crates[-2::-1], moves


def operate_cranemover(stacks, moves, version=9000):
    for times, fro, to in moves:
        fro, to = fro - 1, to - 1
        new_stack = [stacks[fro].pop() for _ in range(times)]
        if version == 9000:
            stacks[to] += new_stack
        elif version == 9001:
            stacks[to] += reversed(new_stack)
    print("".join([stack[-1] for stack in stacks]))


def main():
    layers, moves = read_input()
    stacks = [[] for _ in layers[0]]
    for layer in layers:
        for i, crate in enumerate(layer):
            if crate == " ":
                continue
            stacks[i].append(crate)
    operate_cranemover(deepcopy(stacks), moves, 9000)
    operate_cranemover(deepcopy(stacks), moves, 9001)


if __name__ == "__main__":
    main()
