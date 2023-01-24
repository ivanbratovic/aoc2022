import re
import itertools

test_input = False

all_distances = {}


def line_to_valve(line):
    line = re.split(r"[ ;=,]", line.strip())
    valve, flow, tunnels = line[1], int(line[5]), line[11::2]
    return valve, flow, tunnels


def read_input():
    filename = "inputs/day16-input.txt"
    if test_input:
        filename = "inputs/day16-test.txt"
    with open(filename, "r") as file:
        return list(map(line_to_valve, file.readlines()))


def populate_distances(valves):
    global all_distances
    for start, _, _ in valves:
        # Dijsktra's
        distances = {start: 0}
        unvisited = {valve for valve, _, _ in valves}
        neighbours = {k: v for k, _, v in valves}
        while unvisited:
            current = min(
                {k: v for k, v in distances.items() if k in unvisited},
                key=distances.get,
            )
            unvisited.remove(current)

            for neighbour in neighbours[current]:
                new_dist = distances[current] + 1
                if new_dist < distances.setdefault(neighbour, 10e10):
                    distances[neighbour] = new_dist
        for k, v in distances.items():
            all_distances[start, k] = v


def best_pressure(closed_valves, flows, current, current_time):
    max_time = 30
    if current_time >= max_time or not closed_valves:
        return 0
    max_pressure = 0
    for valve in closed_valves:
        time = current_time + all_distances[(current, valve)] + 1
        total_pressure = (max_time - time) * flows[valve] + best_pressure(
            closed_valves - {valve}, flows, valve, time
        )
        max_pressure = max(max_pressure, total_pressure)
    return max_pressure


def main():
    valves = read_input()
    populate_distances(valves)

    valve_flows = {valve: flow for valve, flow, _ in valves}
    closed_valves = {k for k, v in valve_flows.items() if v > 0}

    print(best_pressure(closed_valves, valve_flows, "AA", 0))

    max_pressure = 0
    for number_of_my_valves in range(1, len(closed_valves)):
        for my_valves in map(
            set, itertools.combinations(closed_valves, number_of_my_valves)
        ):
            my_pressure = best_pressure(my_valves, valve_flows, "AA", 4)
            el_pressure = best_pressure(closed_valves - my_valves, valve_flows, "AA", 4)
            max_pressure = max(max_pressure, my_pressure + el_pressure)

    print(max_pressure)


if __name__ == "__main__":
    main()
