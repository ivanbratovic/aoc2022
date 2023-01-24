import re
import itertools

test_input = False
resource_types = ("ore", "clay", "obsidian", "geode")
current_maximum = 0


def line_to_blueprint(line):
    line = re.split(r" *(Each|costs|and) *", line.strip())
    blueprint = {}
    for robot in resource_types:
        costs = {}
        idx = line.index(f"{robot} robot")
        for i in itertools.count(idx):
            info = line[i]
            if re.match(r"[0-9]+.*", info):
                end = False
                cost, typ = tuple(info.split())
                if typ[-1] == ".":
                    typ = typ[:-1]
                    end = True
                costs[typ] = int(cost)
                if end:
                    break
            if info == "Each":
                break
        blueprint[robot] = costs
    return blueprint


def buy(robot, costs, resources):
    for resource, cost in costs[robot].items():
        resources[resource] -= cost
    return True


def time_to_build(robot, costs, resources, robots):
    time = 0
    for resource, cost in costs[robot].items():
        have = resources[resource]
        robot_count = robots[resource]
        if not robot_count:
            return 999
        if cost > have:
            minutes, remaining = divmod(cost - resources[resource], robot_count)
            time = max(time, minutes + int(remaining > 0))
    return time


def most_geodes(blueprint, start_robots, start_resouces, max_time=24, action="wait"):
    global current_maximum

    if max_time == 0:
        return start_resouces["geode"]
    robots = dict(start_robots)
    resources = start_resouces

    possible_earnings = resources["geode"] + max_time * robots["geode"]

    # if max_time == 1:
    #    return possible_earnings

    max_earnings = possible_earnings + (max_time - 1) * max_time // 2 + 2

    if current_maximum >= max_earnings:
        return possible_earnings

    if action != "wait":
        buy(action, blueprint, resources)
        can_build = []
    else:
        can_build = [
            robot
            for robot in blueprint
            if time_to_build(robot, blueprint, resources, robots) == 0
        ]

    for robot, count in robots.items():
        resources[robot] += count

    if action != "wait":
        robots[action] += 1

    possible_outcomes = []
    for next_action in reversed(
        [
            robot
            for robot, costs in blueprint.items()
            if all([resources[typ] >= cost for typ, cost in costs.items()])
        ]
    ):
        if action == "wait" and next_action in can_build:
            continue
        if robots[next_action] >= max(
            [c[next_action] for c in blueprint.values() if next_action in c],
            default=100,
        ):
            continue
        outcome = most_geodes(
            blueprint, robots, dict(resources), max_time - 1, next_action
        )
        possible_outcomes.append(outcome)
    possible_outcomes.append(
        most_geodes(blueprint, robots, dict(resources), max_time - 1)
    )
    best = max(possible_outcomes)
    current_maximum = max(best, current_maximum)

    return best


def read_input():
    filename = "inputs/day19-input.txt"
    if test_input:
        filename = "inputs/day19-test.txt"
    with open(filename, "r") as file:
        return list(map(line_to_blueprint, file.readlines()))


def main():
    global current_maximum
    max_time = 24
    blueprints = read_input()
    sum_quality = 0
    for i, blueprint in enumerate(blueprints):
        current_maximum = 0
        geodes = most_geodes(
            blueprint,
            {typ: (1 if typ == "ore" else 0) for typ in resource_types},
            {typ: 0 for typ in resource_types},
            max_time=max_time,
        )
        sum_quality += (i + 1) * geodes
    print(sum_quality)
    max_time = 32
    prod_geodes = 1
    for i, blueprint in enumerate(blueprints[:3]):
        current_maximum = 0
        geodes = most_geodes(
            blueprint,
            {typ: (1 if typ == "ore" else 0) for typ in resource_types},
            {typ: 0 for typ in resource_types},
            max_time=max_time,
        )
        prod_geodes *= geodes
    print(prod_geodes)


if __name__ == "__main__":
    main()
    # cProfile.run('main()')
