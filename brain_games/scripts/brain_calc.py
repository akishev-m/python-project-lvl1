#!/usr/bin/env python

import brain_games.games.calc


def main():
    user_name = brain_games.games.calc.welcome_user()
    print('Answer the question')
    quest_num = 0
    while quest_num < 3:
        exp = brain_games.games.calc.calc()  # expected answer
        answer = ''
        while (answer == '') and True:
            try:
                answer = int(input('Your answer: '))
            except ValueError:
                print('Please enter integer.')
                continue
            else:
                break
        quest_num += brain_games.games.calc.is_correct(answer, exp, user_name)
        if quest_num == 3:
            print('Congratulations, ' + user_name)


if __name__ == '__main__':
    main()
