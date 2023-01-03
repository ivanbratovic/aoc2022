test = False

def read_input():
    global test
    filename = "inputs/day01-input.txt"
    if test:
        filename = "inputs/day01-test.txt"
    with open(filename, "r") as file:
        return file.readlines()

def get_calories():
    calories_by_elf = [0]
    idx = 0
    for line in read_input():
        try:
            calories_by_elf[idx] += int(line)
        except ValueError:
            idx += 1
            calories_by_elf.append(0)
    return calories_by_elf

def main():
    print(max(get_calories()))
    print(sum(sorted(get_calories(), reverse=True)[:3]))

if __name__ == "__main__":
    main()
