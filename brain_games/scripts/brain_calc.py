#!/usr/bin/env python

from brain_games.games.calc import calc
from brain_games.games.common import welcome_user, ansr_int, game


def main():
    user_name = welcome_user()
    print('Answer the question')
    game(user_name, ansr_int, calc)


if __name__ == '__main__':
    main()
