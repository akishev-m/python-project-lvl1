#!/usr/bin/env python

import prompt


# Compare user answer with expected and show relevant message
def is_correct(answer, exp, user_name):
    if str(answer) == str(exp):
        print('Correct!')
        return True
    else:
        print('\"' + str(answer) + '\" is wrong ;(. \
Correct answer is \"' + str(exp) + '\".')
        print('Let\'s try again, ' + user_name + '!')
        return False


# Input data: game
# optional - quesstions number (3 by default)
def game(f_game, questions=3):
    print("Welcome to the Brain Games!")  # greeting
    user_name = ''
    while user_name == '':
        user_name = prompt.string('May I have your name? ')
        print('Hello, ' + user_name + '!')
    print(f_game('TASK'))  # getting task and print it for user
    quest_num = 0
    while quest_num < questions:
        print('Question: ', end='')
        exp_answer = f_game()  # show game data & get expect ansr
        user_answer = ''
        while (user_answer == '') and True:
            user_answer = prompt.string('Your answer: ')
        if is_correct(user_answer, exp_answer, user_name):
            quest_num += 1
            if quest_num == 3:
                print('Congratulations, ' + user_name + '!')
        else:
            break
