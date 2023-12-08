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
    match len(counter):
        case 0:
            # - / JJJJJ
            return HandType.FIVE_OF_A_KIND
        case 1:
            # AAAAA / {J}{A}
            return HandType.FIVE_OF_A_KIND
        case 2:
            if counter.most_common()[-1][1] == 1:
                # AAAAB / {J}{A}B
                return HandType.FOUR_OF_A_KIND
            else:
                # AAABB / {J}AABB
                return HandType.FULL_HOUSE
        case 3:
            if counter.most_common()[-2][1] == 1:
                # AAABC / {J}{A}BC
                return HandType.THREE_OF_A_KIND
            else:
                # AABBC / -
                return HandType.TWO_PAIR
        case 4:
            # AABCD / {J}ABCD
            return HandType.ONE_PAIR
        case _:
            # ABCDE / -
            return HandType.HIGH_CARD


def solve_part1(cards: list[(str, int)]) -> int:
    order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    # x = (hand, bid)
    cards.sort(key=lambda x: (hand_to_type(x[0]), hand_to_nums(x[0], order)), reverse=True)
    return sum([i * x[1] for i, x in enumerate(cards, 1)])


def solve_part2(cards: list[(str, int)]) -> int:
    order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    cards.sort(key=lambda x: (hand_to_type(x[0].replace('J', '')), hand_to_nums(x[0], order)), reverse=True)
    return sum([i * x[1] for i, x in enumerate(cards, 1)])


if __name__ == '__main__':
    # Read the input data
    data = list(read_input("input.txt"))

    # Solve part 1
    part1_answer = solve_part1(data)
    print("Part 1:", part1_answer)

    # Solve part 2
    part2_answer = solve_part2(data)
    print("Part 2:", part2_answer)
