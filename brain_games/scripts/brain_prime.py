#!/usr/bin/env python

from brain_games.game_engine import game
from brain_games.games.prime import prime


def main():
    game('Answer "yes" if given number is prime. Otherwise answer "no".', prime)


if __name__ == '__main__':
    main()
