from dataclasses import dataclass
import numpy as np
import math
test_input = False

@dataclass
class Monkey:
    items: list
    operation: str
    test: int
    false_action: int
    true_action: int

def read_input():
    global test_input
    filename = "inputs/day11-input.txt"
    if test_input:
        filename = "inputs/day11-test.txt"
    monkeys = []
    with open(filename, "r") as file:
        current_monkey = {}
        for line in file.readlines():
            match line.strip().split():
                case ["Starting", "items:", *items]:
                    current_monkey["items"] = list(map(lambda x: int(x.replace(",", "")), items))
                case ["Operation:", *operation]:
                    current_monkey["operation"] = " ".join(operation[2:])
                case ["Test:", "divisible", "by", test]:
                    current_monkey["test"] = int(test)
                case ["If", condition, "throw", "to", "monkey", num]:
                    if condition == "true:":
                        current_monkey["true_action"] = int(num)
                    else:
                        current_monkey["false_action"] = int(num)
                case []:
                    monkeys.append(Monkey(**current_monkey))
    monkeys.append(Monkey(**current_monkey))
    return monkeys

def one_round(monkeys, counts, modulus=0):
    for i, monkey in enumerate(monkeys):
        counts[i] += len(monkey.items)
        for _ in range(len(monkey.items)):
            old = monkey.items.pop(0)
            new = eval(monkey.operation)
            if modulus:
                new = new % modulus
            else:
                new = new // 3
            throw_to_monkey = monkey.false_action
            if new % monkey.test == 0:
                throw_to_monkey = monkey.true_action
            monkeys[throw_to_monkey].items.append(new)

def monkey_business(round_count, use_modulus):
    monkeys = read_input()
    counts = np.zeros_like(monkeys, dtype=int)
    if use_modulus:
        modulus = math.prod([monkey.test for monkey in monkeys])
    else:
        modulus = 0
    [one_round(monkeys, counts, modulus) for _ in range(round_count)]
    print(math.prod(sorted(counts)[-2:]))

def main():
    monkey_business(20, False)
    monkey_business(10000, True)


if __name__ == "__main__":
    main()