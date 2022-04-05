#!/usr/bin/env python

from brain_games.games.common import welcome_user, ansr_int, game
from brain_games.games.progression import progression


# welcome_user() - greeting and get user name
# ansr_int() - get answer and compare with expected
# progression() - suggest question and calculate expected answer
# game() - combine games elements


def main():
    user_name = welcome_user()
    print('What number is missing in the progression?')
    game(user_name, ansr_int, progression)


if __name__ == '__main__':
    main()
