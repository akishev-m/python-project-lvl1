#!/usr/bin/env python

from brain_games.game_engine import run_game
from brain_games.games.progression import generate_progression_round, QUESTION


def main():
    run_game(QUESTION, generate_progression_round)


if __name__ == '__main__':
    main()
