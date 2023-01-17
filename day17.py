test_input = False

def read_input():
    filename = "inputs/day17-input.txt"
    if test_input:
        filename = "inputs/day17-test.txt"
    with open(filename, "r") as file:
        return file.readline().strip()

def invalid_pos(piece, coords, points):
    x, y = coords
    for dx, dy in piece:
        x0, y0 = x + dx, y + dy
        if (x0, y0) in points:
            return True
        if x0 not in range(0, 7):
            return True
        if y0 < 0:
            return True
    return False

def manhattan_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def drop_piece(piece, coords, points, direction):
    x, y = coords
    if direction == "<":
        dx = -1
    else:
        dx = +1
    if not invalid_pos(piece, (x + dx, y), points):
        x += dx
    if invalid_pos(piece, (x, y - 1), points):
        for dx, dy in piece:
            points.add((x + dx, y + dy))
        return True, coords
    return False, (x, y - 1)

def print_map(points, tallest_point):

    def shortprint(*args, **kwargs):
        print(*args, **kwargs, end="")
    
    for y in range(tallest_point + 4, 0, -1):
        shortprint(f"\n{y:-4} |")
        for x in range(7):
            point = (x, y)
            if point in points:
                shortprint("#")
            else:
                shortprint(".")
        shortprint("|")
    print("\n   0 +-------+")

def drop_pieces(n=2022):
    directions = read_input()
    pieces = [
        ((0, 0), (1, 0), (2, 0), (3, 0)),
        ((0, 1), (1, 0), (2, 1), (1, 1), (1, 2)),
        ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)),
        ((0, 0), (0, 1), (0, 2), (0, 3)),
        ((0, 0), (1, 0), (0, 1), (1, 1))
    ]
    points = {(i, 0) for i in range(7)}
    states = {}
    jet_step = 0
    for i in range(n):
        piece = pieces[i % 5]
        coords = (2, max(points, key=lambda x: x[1])[1] + 4)
        start = coords
        dropped = False
        while not dropped:
            dropped, coords = drop_piece(piece, coords, points, directions[jet_step])
            jet_step = (jet_step + 1) % len(directions)
        state = (i % 5, jet_step, manhattan_dist(start, coords), coords[0])
        tallest_point = max(points, key=lambda x: x[1])[1]
        if state in states:
            previous_i, prev_height = states[state]
            cycle_count, remain = divmod(n - i - 1, i - previous_i)
            if remain == 0:
                print((tallest_point - prev_height) * cycle_count + tallest_point)
                return
        else:
            states[state] = i, tallest_point
    print(tallest_point)

def main():
    drop_pieces(n=2022)
    drop_pieces(n=1000000000000)
    

if __name__ == "__main__":
    main()