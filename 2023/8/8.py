import math
import re


def read_input(filename: str) -> tuple[str, dict[str, (str, str)]]:
    # Read input from a file and return processed data.
    with open(filename, 'r') as f:
        sequence = f.readline().strip()
        f.readline()
        nodes = dict()
        for line in f:
            line = re.sub(r"[=(,)]", ' ', line)
            s, l, r = line.split()
            nodes[s] = (l, r)
        return sequence, nodes


def find_len(start: str, end_predicate, sequence: str, nodes: dict[str, (str, str)]) -> int:
    cur = start
    i = 0
    while not end_predicate(cur):
        cur = nodes[cur][0] if sequence[i % len(sequence)] == 'L' else nodes[cur][1]
        i += 1
    return i


def solve_part1(data: tuple[str, dict[str, (str, str)]]) -> int:
    sequence, nodes = data
    return find_len('AAA', lambda x: x == 'ZZZ', sequence, nodes)


def solve_part2(data: tuple[str, dict[str, (str, str)]]) -> int:
    sequence, nodes = data
    curs = [node for node in nodes if node[-1] == 'A']
    return math.lcm(*[find_len(cur, lambda x: x[-1] == 'Z', sequence, nodes) for cur in curs])


if __name__ == '__main__':
    # Read the input data
    data = read_input("input.txt")

    # Solve part 1
    part1_answer = solve_part1(data)
    print("Part 1:", part1_answer)

    # Solve part 2
    part2_answer = solve_part2(data)
    print("Part 2:", part2_answer)
