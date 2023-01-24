import re

test_input = True


def manhattan_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def line_to_coords(line):
    line = re.split(r"[ ,=:]", line)
    sensor = int(line[3]), int(line[6])
    beacon = int(line[13]), int(line[16])
    return sensor, beacon, manhattan_dist(sensor, beacon)


def read_input():
    global test_input
    filename = "inputs/day15-input.txt"
    if test_input:
        filename = "inputs/day15-test.txt"
    with open(filename, "r") as file:
        return list(map(line_to_coords, file.readlines()))


def horizontal_dist(a, b):
    return abs(a[0] - b[0])


def point_can_be_beacon(point, coords):
    for sensor, _, distance in coords:
        if manhattan_dist(point, sensor) <= distance:
            return False, sensor, distance
    return True, None, None


def print_map(beacons, sensors, coords, min_point, max_point):
    for y in range(min_point[1], max_point[1]):
        print(f"{y:3} ", end="")
        for x in range(min_point[0], max_point[0]):
            point = (x, y)
            if (x, y) in beacons:
                print("B", end="")
            elif (x, y) in sensors:
                print("S", end="")
            elif not point_can_be_beacon(point, coords)[0]:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()


def main():
    global test_input
    coords = read_input()
    sensors = [pair[0] for pair in coords]
    beacons = [pair[1] for pair in coords]
    min_point = coords[0][0]
    max_point = coords[0][0]
    max_distance = 0
    for sensor, beacon, d in coords:
        max_distance = max(d, max_distance)
        min_point = (
            min(min_point[0], sensor[0], beacon[0]),
            min(min_point[1], sensor[1], beacon[1]),
        )
        max_point = (
            max(max_point[0], sensor[0], beacon[0]),
            max(max_point[1], sensor[1], beacon[1]),
        )
    min_point = (min_point[0] - max_distance, min_point[1] - max_distance)
    max_point = (max_point[0] + max_distance, max_point[1] + max_distance)

    y = 2000000
    if test_input:
        y = 10
        print_map(beacons, sensors, coords, min_point, max_point)

    s = 0
    x = min_point[0]
    while x < max_point[0]:
        point = (x, y)
        possible, sensor, d_sb = point_can_be_beacon(point, coords)
        if not possible:
            two_dx_ps = horizontal_dist(point, sensor) * 2
            d_ps = manhattan_dist(point, sensor)
            # Skip to end of nearest sensor's range
            if x < sensor[0]:
                x += two_dx_ps
                s += two_dx_ps
            x += d_sb - d_ps
            s += d_sb - d_ps + 1
        x += 1

    print(s - 1)  # Part one

    min_point = (0, 0)
    max_point = (4_000_000, 4_000_000)
    if test_input:
        max_point = (20, 20)

    for y in range(min_point[1], max_point[1]):
        x = min_point[0]
        while x <= max_point[0]:
            point = (x, y)
            possible, sensor, d_sb = point_can_be_beacon(point, coords)
            if possible:
                print(x * 4_000_000 + y)  # Part 2
                return
            # Skip to end of nearest sensor's range
            if x < sensor[0]:
                x += 2 * horizontal_dist(point, sensor)
            x += d_sb - manhattan_dist(point, sensor) + 1


if __name__ == "__main__":
    main()
