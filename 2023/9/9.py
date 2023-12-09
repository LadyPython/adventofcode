def read_input(filename: str) -> list[list[int]]:
    # Read input from a file and return processed data.
    with open(filename, 'r') as f:
        return [list(map(int, line.strip().split())) for line in f.readlines()]


def solve_part1(data: list[list[int]]) -> int:
    ans = 0
    for line in data:
        lasts = []
        while sum(line) != 0:
            lasts.append(line[-1])
            line = [line[i + 1] - line[i] for i in range(len(line) - 1)]
        ans += sum(lasts)
    return ans


def solve_part2(data: list[list[int]]) -> int:
    ans = 0
    for line in data:
        firsts = []
        while sum(line) != 0:
            firsts.append(line[0])
            line = [line[i + 1] - line[i] for i in range(len(line) - 1)]
        ans += sum(firsts[::2]) - sum(firsts[1::2])
    return ans


if __name__ == '__main__':
    # Read the input data
    data = read_input("input.txt")

    # Solve part 1
    part1_answer = solve_part1(data)
    print("Part 1:", part1_answer)

    # Solve part 2
    part2_answer = solve_part2(data)
    print("Part 2:", part2_answer)
