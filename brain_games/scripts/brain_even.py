#!/usr/bin/env python

import brain_games.games.even
import prompt


def main():
    user_name = brain_games.games.even.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    quest_num = 0
    while quest_num < 3:
        exp = brain_games.games.even.is_even()  # expected answer
        ansr = ''
        while ansr == '':
            ansr = prompt.string('Your answer: ')
            quest_num += brain_games.games.even.is_correct(ansr, exp, user_name)
            if quest_num == 3:
                print('Congratulations, ' + user_name + '!')


if __name__ == '__main__':
    main()
