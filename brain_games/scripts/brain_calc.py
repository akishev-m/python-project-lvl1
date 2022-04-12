#!/usr/bin/env python

from brain_games.game_engine import game
from brain_games.games.calc import calc


def main():
    game('Answer the question', calc)


if __name__ == '__main__':
    main()
