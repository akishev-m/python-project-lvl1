#!/usr/bin/env python

from brain_games.games.common import welcome_user, ansr_int, game
from brain_games.games.gcd import gcd


# welcome_user() - greeting and get user name
# ansr_int() - get answer and compare with expected
# gcd() - suggest question and calculate expected answer
# game() - combine games elements


def main():
    user_name = welcome_user()
    print('Find the greatest common division of given numbers.')
    game(user_name, ansr_int, gcd)


if __name__ == '__main__':
    main()
