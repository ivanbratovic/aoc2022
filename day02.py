test = False

scores = {"A": 1, "B": 2, "C": 3}
draws = {"X": "A", "Y": "B", "Z": "C"}
beats = {"A": "C", "B": "A", "C": "B"}
loses = {v: k for k, v in beats.items()}
win_score = 6
draw_score = 3


def read_input():
    global test
    filename = "inputs/day02-input.txt"
    if test:
        filename = "inputs/day02-test.txt"
    with open(filename, "r") as file:
        return [(line[0], line[2]) for line in file.readlines()]


def main():
    score = 0
    for p1, p2 in read_input():
        p2 = draws[p2]
        score += scores[p2]
        if beats[p2] == p1:
            score += win_score
        elif p1 == p2:
            score += draw_score
    print(score)
    score = 0
    for p1, p2 in read_input():
        if p2 == "Z":  # Win
            score += win_score
            score += scores[loses[p1]]
        if p2 == "Y":  # Draw
            score += draw_score
            score += scores[p1]
        if p2 == "X":  # Loss
            score += scores[beats[p1]]
    print(score)


if __name__ == "__main__":
    main()
