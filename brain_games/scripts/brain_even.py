#!/usr/bin/env python

from brain_games.game_engine import game
from brain_games.games.even import even_game_round

QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    game(QUESTION, even_game_round)


if __name__ == '__main__':
    main()
