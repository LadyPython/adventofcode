from collections import Counter
from enum import IntEnum


class HandType(IntEnum):
    FIVE_OF_A_KIND = 1
    FOUR_OF_A_KIND = 2
    FULL_HOUSE = 3
    THREE_OF_A_KIND = 4
    TWO_PAIR = 5
    ONE_PAIR = 6
    HIGH_CARD = 7


def read_input(filename: str):
    # Read input from a file and return processed data.
    with open(filename, 'r') as f:
        for line in f:
            hand, bid = line.split()
            yield hand, int(bid)


def hand_to_nums(hand: str, order: list[str]) -> tuple[int, ...]:
    return tuple(map(lambda x: order.index(x), list(hand)))


def hand_to_type(hand: str) -> HandType:
    counter = Counter(hand)
    if len(counter) == 2 and counter.most_common()[-1][1] != 1:
        return HandType.FULL_HOUSE
    elif len(counter) == 3 and counter.most_common()[-2][1] != 1:
        return HandType.TWO_PAIR
    hand_types = [
        HandType.FIVE_OF_A_KIND,
        HandType.FOUR_OF_A_KIND,
        HandType.THREE_OF_A_KIND,
        HandType.ONE_PAIR,
        HandType.HIGH_CARD
    ]
    return hand_types[max(len(counter) - 1, 0)]


def solve_part1(cards: list[(str, int)]) -> int:
    order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    # x = (hand, bid)
    cards.sort(key=lambda x: (hand_to_type(x[0]), hand_to_nums(x[0], order)), reverse=True)
    return sum(i * x[1] for i, x in enumerate(cards, 1))


def solve_part2(cards: list[(str, int)]) -> int:
    order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    cards.sort(key=lambda x: (hand_to_type(x[0].replace('J', '')), hand_to_nums(x[0], order)), reverse=True)
    return sum(i * x[1] for i, x in enumerate(cards, 1))


if __name__ == '__main__':
    # Read the input data
    data = list(read_input("input.txt"))

    # Solve part 1
    part1_answer = solve_part1(data)
    print("Part 1:", part1_answer)

    # Solve part 2
    part2_answer = solve_part2(data)
    print("Part 2:", part2_answer)
