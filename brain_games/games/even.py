#!/usr/bin/env python

import prompt
import random


def welcome_user():
    print("Welcome to the Brain Games!")
    user_name = ''
    while user_name == '':
        user_name = prompt.string('May I have your name? ')
        print('Hello, ' + user_name + '!')
        return user_name


def is_even():
    num = round(random.random() * 10)
    print('Question: ' + str(num))
    return 'yes' if num % 2 == 0 else 'no'


def is_correct(answer, exp, user_name):

    if answer == exp:
        print('Correct!')
    else:
        print('\"' + str(answer) + '\" is wrong ;(. \
Correct answer is \"' + str(exp) + '\".')
        print('Let\'s try again, ' + user_name + '!')
    return 1 if answer == exp else 4
