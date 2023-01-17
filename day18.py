test_input = False

def read_input():
    filename = "inputs/day18-input.txt"
    if test_input:
        filename = "inputs/day18-test.txt"
    with open(filename, "r") as file:
        return list(map(lambda l: tuple(map(int ,l.strip().split(","))), file.readlines()))

def neighbours(point):
    x, y, z = point
    for d in (-1, 1):
        for neigh in [(x + d, y, z), (x, y + d, z), (x, y, z + d)]:
            yield neigh

calculated_pockets = set()
def is_air_pocket(point, points):
    # Basic fill algorithm
    global calculated_pockets
    if point in calculated_pockets:
        return True
    if point in points:
        return False
    fill = {point}
    visited = set()
    while fill:
        current = fill.pop()
        visited.add(current)

        if len(visited) > len(points):
            return False

        for neigh in neighbours(current):
            if neigh not in points and neigh not in visited:
                fill.add(neigh)
    
    for air in visited:
        calculated_pockets.add(air)

    return True


def main():
    points = set(read_input())
    shared_sides = 0
    pocket_sides = 0
    for x, y, z in points:
        for neigh in neighbours((x,y,z)):
            if neigh in points:
                shared_sides += 1
            elif is_air_pocket(neigh, points):
                pocket_sides += 1
    
    print(len(points) * 6 - shared_sides)
    print(len(points) * 6 - shared_sides - pocket_sides)


if __name__ == "__main__":
    main()