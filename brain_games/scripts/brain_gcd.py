#!/usr/bin/env python

from brain_games.game_engine import game
from brain_games.games.gcd import gcd


def main():
    game('Find the greatest common division of given numbers.', gcd)


if __name__ == '__main__':
    main()
