#!/usr/bin/env python

from brain_games.games.even import is_even
from brain_games.games.common import welcome_user, ansr_str, game


def main():
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    game(user_name, ansr_str, is_even)


if __name__ == '__main__':
    main()
