#!/usr/bin/env python

from brain_games.game_engine import game
from brain_games.games.prime import prime_game_round

QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    game(QUESTION, prime_game_round)


if __name__ == '__main__':
    main()
