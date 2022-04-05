#!/usr/bin/env python

import prompt


# Greeting and getting Username
def welcome_user():
    print("Welcome to the Brain Games!")
    user_name = ''
    while user_name == '':
        user_name = prompt.string('May I have your name? ')
        print('Hello, ' + user_name + '!')
        return user_name


# Compare user answer with expected and show relevant message
def is_correct(answer, exp, user_name):
    if answer == exp:
        print('Correct!')
    else:
        print('\"' + str(answer) + '\" is wrong ;(. \
Correct answer is \"' + str(exp) + '\".')
        print('Let\'s try again, ' + user_name + '!')
    return 1 if answer == exp else 4


# Get integer user answer and check if it is integer
def ansr_int():
    ansr = ''
    while (ansr == '') and True:
        try:
            ansr = int(input('Your answer: '))
        except ValueError:
            print('Please enter integer.')
            continue
        else:
            break
    return ansr


# Get string user anser
def ansr_str():
    ansr = ''
    while (ansr == '') and True:
        try:
            ansr = prompt.string('Your answer: ')
        except ValueError:
            print('Please enter string.')
            continue
        else:
            break
    return ansr


# Input data: username, function of getting answer (for int or str)
# and function of type os game and relevant expexted answer
# optional - quesstions number (3 by default)
def game(user_name, f_ansr, f_exp, questions=3):
    quest_num = 0
    while quest_num < questions:
        e = f_exp()
        a = f_ansr()
        quest_num += is_correct(a, e, user_name)
        if quest_num == 3:
            print('Congratulations, ' + user_name + '!')
