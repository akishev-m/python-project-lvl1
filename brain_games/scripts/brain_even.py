#!/usr/bin/env python

from brain_games.games.common import game
from brain_games.games.even import is_even


def main():
    game('Answer "yes" if the number is even, otherwise answer "no".', is_even)


if __name__ == '__main__':
    main()
