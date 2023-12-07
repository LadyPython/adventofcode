
def read_input(filename: str) -> (list[int], list[int]):
    # Read input from a file and return processed data.
    with open(filename, 'r') as f:
        times = list(map(int, f.readline().strip().split()[1:]))
        distances = list(map(int, f.readline().strip().split()[1:]))
        return times, distances


def number_of_ways_to_beat(time: int, distance: int) -> int:
    d = time ** 2 - 4 * distance
    x_max = int((time + d ** 0.5) / 2)
    x_min = int((time - d ** 0.5) / 2 + 1)
    return x_max - x_min + 1


def solve_part1(data: (list[int], list[int])) -> int:
    answer = 1
    for time, distance in zip(*data):
        answer *= number_of_ways_to_beat(time, distance)
    return answer


def solve_part2(data: list[(int, int)]) -> int:
    times, distances = data
    time = int(''.join(map(str, times)))
    distance = int(''.join(map(str, distances)))
    return number_of_ways_to_beat(time, distance)


if __name__ == '__main__':
    # Read the input data
    data = read_input("input.txt")

    # Solve part 1
    part1_answer = solve_part1(data)
    print("Part 1:", part1_answer)

    # Solve part 2
    part2_answer = solve_part2(data)
    print("Part 2:", part2_answer)
