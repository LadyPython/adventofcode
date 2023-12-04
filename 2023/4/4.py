from collections import defaultdict
import re


def read_input(filename: str) -> list[(int, set, set)]:
    # Read input from a file and return processed data.
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            pattern = re.compile(r"Card\s+(?P<id>\d+): (?P<win_cards>.*) \| (?P<all_cards>.*)")
            match = pattern.match(line)

            card_id = int(match.group('id'))
            win_cards = set(match.group('win_cards').split())
            all_cards = set(match.group('all_cards').split())
            data.append((card_id, win_cards, all_cards))
    return data


def solve_part1(data: list[(int, set, set)]) -> int:
    answer = 0
    for card_id, win_cards, all_cards in data:
        matching_num = sum(card in all_cards for card in win_cards)
        answer += 2 ** (matching_num - 1) if matching_num > 0 else 0
    return answer


def solve_part2(data: list[(int, set, set)]) -> int:
    card_to_num = defaultdict(lambda: 1)
    for card_id, win_cards, all_cards in data:
        matching_num = sum(card in all_cards for card in win_cards)
        for new_card_id in range(card_id + 1, card_id + matching_num + 1):
            card_to_num[new_card_id] += card_to_num[card_id]
    return sum(card_to_num.values())


if __name__ == '__main__':
    # Read the input data
    data = read_input("input.txt")

    # Solve part 1
    part1_answer = solve_part1(data)
    print("Part 1:", part1_answer)

    # Solve part 2
    part2_answer = solve_part2(data)
    print("Part 2:", part2_answer)
