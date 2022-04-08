#!/usr/bin/env python

from brain_games.games.common import game
from brain_games.games.calc import calc


def main():
    game('Answer the question', calc)


if __name__ == '__main__':
    main()
