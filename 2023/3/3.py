import re


class Board:
    def __init__(self, data: list[str]):
        self.data = data
        self.height = len(data)
        self.width = len(data[0])

    def __getitem__(self, x: int) -> str:
        return self.data[x]

    def on_board(self, x: int, y: int) -> bool:
        return 0 <= x < self.height and 0 <= y < self.width


def read_input(filename: str) -> Board:
    # Read input from a file and return processed data.
    with open(filename, 'r') as f:
        return Board([line.strip() for line in f.readlines()])


def solve_part1(board: Board) -> int:
    def is_symbol(c: str) -> bool:
        return c != '.' and not c.isdigit()

    def is_connected(x: int, ys: (int, int), board: Board) -> bool:
        y_start, y_end = ys
        y_end -= 1
        # (x - 1, y_start - 1) (x - 1, y_start) (x - 1, y_start + 1) ... (x - 1, y_end + 1)
        # (x    , y_start - 1)                                           (x    , y_end + 1)
        # (x + 1, y_start - 1) (x + 1, y_start) (x + 1, y_start + 1) ... (x + 1, y_end + 1)

        neighbours = [(nx, ny) for nx in range(x - 1, x + 2) for ny in range(y_start - 1, y_end + 2)
                      if not (nx == x and y_start <= ny <= y_end)]

        for nx, ny in neighbours:
            if board.on_board(nx, ny) and is_symbol(board[nx][ny]):
                return True
        return False

    answer = 0
    for i, line in enumerate(board):
        for it in re.finditer(r"\d+", line):
            answer += is_connected(i, it.span(), board) * int(it.group())
    return answer


def solve_part2(board: Board) -> int:
    answer = 0
    for i, line in enumerate(board):
        for j, c in enumerate(line):
            if c != '*':
                continue

            neighbour_strs = [line]
            if i > 0:
                neighbour_strs.append(board[i - 1])
            if i < board.height - 1:
                neighbour_strs.append(board[i + 1])

            neighbour_ints = []
            for s in neighbour_strs:
                for it in re.finditer(r"\d+", s):
                    start, end = it.span()  # [start, end)
                    if start - 1 <= j <= end:
                        neighbour_ints.append(int(it.group()))
            
            if len(neighbour_ints) == 2:
                answer += neighbour_ints[0] * neighbour_ints[1]
                print(neighbour_ints[0], neighbour_ints[1])
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
