#!/usr/bin/env python

from brain_games.games.common import welcome_user, ansr_int, game
from brain_games.games.calc import calc

# welcome_user() - greeting and get user name
# ansr_int() - get answer and compare with expected
# calc() - suggest question and calculate expected answer
# game() - combine games elements


def main():
    user_name = welcome_user()
    print('Answer the question')
    game(user_name, ansr_int, calc)


if __name__ == '__main__':
    main()
