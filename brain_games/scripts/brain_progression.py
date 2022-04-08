#!/usr/bin/env python

from brain_games.games.common import game
from brain_games.games.progression import progression


def main():
    game('What number is missing in the progression?', progression)


if __name__ == '__main__':
    main()
