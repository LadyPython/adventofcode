import re

COLORS = ['red', 'green', 'blue']


def read_input(filename: str) -> dict:
    def parse_subset(subset: str) -> dict:
        # Parse a subset of the form '3 red, 2 green, 1 blue' into a dictionary {'red': 3, 'green': 2, 'blue': 1}
        subset_dict = dict()
        for color in COLORS:
            color_pattern = rf"(?P<num>\d+) {color}"
            match = re.search(color_pattern, subset)
            subset_dict[color] = int(match.group('num')) if match else 0

        return subset_dict

    # Read input from a file and return processed data.
    with open(filename, 'r') as f:
        # Parse the input data
        games = dict()
        for line in f.readlines():
            pattern = re.compile(r"Game (?P<game_id>\d+): (?P<sets>.*)")
            match = pattern.match(line)

            game_id = int(match.group('game_id'))
            sets = [parse_subset(subset) for subset in match.group('sets').split('; ')]

            games[game_id] = sets

        # Return the processed data
        return games


def solve_part1(data: dict) -> int:
    max_colors = {'red': 12, 'green': 13, 'blue': 14}

    answer = 0

    for game_id, sets in data.items():
        is_possible = all(subset[color] <= max_colors[color] for color in COLORS for subset in sets)
        answer += is_possible * game_id

    return answer


def solve_part2(data: dict) -> int:
    answer = 0

    for sets in data.values():
        power = 1
        for color in COLORS:
            power *= max(subset[color] for subset in sets)
        answer += power

    return answer


if __name__ == '__main__':
    # Read the input data
    data = read_input("input.txt")

    # Solve part 1
    part1_answer = solve_part1(data)
    print("Part 1:", part1_answer)

    # Solve part 2
    part2_answer = solve_part2(data)
    print("Part 2:", part2_answer)
