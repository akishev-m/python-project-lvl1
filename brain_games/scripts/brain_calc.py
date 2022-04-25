#!/usr/bin/env python

from brain_games.game_engine import game
from brain_games.games.calc import calc_game_round, QUESTION


def main():
    game(QUESTION, calc_game_round)


if __name__ == '__main__':
    main()
