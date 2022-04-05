#!/usr/bin/env python

from brain_games.games.common import welcome_user, ansr_str, game
from brain_games.games.even import is_even


# welcome_user() - greeting and get user name
# ansr_str() - get answer and compare with expected
# is_even() - suggest question and calculate expected answer
# game() - combine games elements


def main():
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    game(user_name, ansr_str, is_even)


if __name__ == '__main__':
    main()
