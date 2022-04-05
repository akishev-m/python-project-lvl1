#!/usr/bin/env python

from brain_games.games.common import welcome_user, ansr_str, game
from brain_games.games.prime import prime


# welcome_user() - greeting and get user name
# ansr_str() - get answer and compare with expected
# prime() - suggest question and calculate expected answer
# game() - combine games elements


def main():
    user_name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise anser "no".')
    game(user_name, ansr_str, prime)


if __name__ == '__main__':
    main()
