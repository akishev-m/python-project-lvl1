#!/usr/bin/env python

from brain_games.games.common import game
from brain_games.games.even import is_even


def main():
    game(is_even)


if __name__ == '__main__':
    main()
