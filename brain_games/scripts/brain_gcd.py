#!/usr/bin/env python

from brain_games.game_engine import run_game
from brain_games.games.gcd import generate_gcd_round, QUESTION


def main():
    run_game(QUESTION, generate_gcd_round)


if __name__ == '__main__':
    main()
