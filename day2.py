from typing import List

from day import Day


def extract_game(line: str) -> List[List[int]]:
    game = []
    for play in line.split(':')[1].split(';'):
        once_list = [0, 0, 0]
        for once in play.strip().split(','):
            once = once.strip()
            num = int(once.split(' ')[0].strip())
            color = once.split(' ')[1].strip()
            if color == 'blue':
                once_list[0] = num
            elif color == 'red':
                once_list[1] = num
            elif color == 'green':
                once_list[2] = num
            else:
                raise Exception(f"bad input:{once}")
            game.append(once_list)
    return game


def possible(line: str) -> bool:
    """
    12 red cubes, 13 green cubes, and 14 blue cubes
    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    :param line:
    """
    for play in extract_game(line):
        if play[0] > 14:
            return False
        elif play[1] > 12:
            return False
        elif play[2] > 13:
            return False
    return True


def sum_of_minimal(line: str) -> int:
    minimal = [0, 0, 0]
    for play in extract_game(line):
        for i in range(3):
            minimal[i] = max(minimal[i], play[i])
    return minimal[0] * minimal[1] * minimal[2]


class Day2(Day):

    def __init__(self):
        super().__init__(day=2)

    def part_one(self, lines: List[str]) -> int:
        ret = 0
        for i, line in enumerate(lines):
            if possible(line):
                ret += i + 1
        return ret

    def part_two(self, lines: List[str]) -> int:
        ret = 0
        for line in lines:
            ret += sum_of_minimal(line)
        return ret


if __name__ == '__main__':
    Day2().run()