test = False

def read_input():
    global test
    filename = "inputs/day03-input.txt"
    if test:
        filename = "inputs/day03-test.txt"
    with open(filename, "r") as file:
        return list(map(lambda x: x.strip(), file.readlines()))

def priority(char: set):
    char = "".join(char)
    n = ord(str(char))
    if n <= 90:
        return n - 38
    return n - 96

def main():
    lines = read_input()
    print(sum([priority(set(r1).intersection(r2)) for r1, r2 in [(line[:len(line)//2], line[len(line)//2:]) for line in lines]]))
    print(sum([priority(set(r1).intersection(r2).intersection(r3)) for r1, r2, r3 in [tuple(lines[i:i+3]) for i in range(0, len(lines), 3)]]))
        
  
if __name__ == "__main__":
    main()
