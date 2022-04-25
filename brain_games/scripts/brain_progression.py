#!/usr/bin/env python

from brain_games.game_engine import game
from brain_games.games.progression import progression_game_round, QUESTION


def main():
    game(QUESTION, progression_game_round)


if __name__ == '__main__':
    main()
