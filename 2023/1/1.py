def read_input(filename: str) -> list[str]:
    # Read input from a file and return processed data.
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]


def solve_part1(data: list[str]) -> int:
    def find_calibration_value(line: str) -> int:
        # Find the first and the last digit in the line, combine them as 'first' + 'last'
        digits = [char for char in line if char.isdigit()]
        return int(digits[0] + digits[-1])

    return sum(find_calibration_value(line) for line in data)


def solve_part2(data: list[str]) -> int:
    word_to_digit = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    def find_digit(line: str, word_to_digit: dict) -> str:
        # Find the first digit in the line even if it is written as a word
        for i, char in enumerate(line):
            if char.isdigit():
                return char

            for word, digit in word_to_digit.items():
                if line[i:i + len(word)] == word:
                    return digit

    def rfind_digit(line: str, word_to_digit: dict) -> str:
        # Find the last digit in the line even if it is written as a word
        return find_digit(line[::-1], {word[::-1]: digit for word, digit in word_to_digit.items()})

    def find_calibration_value(line: str) -> int:
        # Find the first and the last digit in the line, combine them as 'first' + 'last'
        return int(find_digit(line, word_to_digit) + rfind_digit(line, word_to_digit))

    return sum(find_calibration_value(line) for line in data)


if __name__ == '__main__':
    # Read the input data
    data = read_input("input.txt")

    # Solve part 1
    part1_answer = solve_part1(data)
    print("Part 1:", part1_answer)

    # Solve part 2
    part2_answer = solve_part2(data)
    print("Part 2:", part2_answer)
