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


def is_correct(answer, exp, user_name):
    if answer == exp:
        print('Correct!')
    else:
        print('\"' + str(answer) + '\" is wrong ;(. \
Correct answer is \"' + str(exp) + '\".')
        print('Let\'s try again, ' + user_name + '!')
    return 1 if int(answer) == int(exp) else 4


def calc():
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    opperation = random.randint(1, 3)
    c = None
    if opperation == 1:
        print('Question: ' + str(a) + ' + ' + str(b))
        c = a + b
    elif opperation == 2:
        print('Question: ' + str(a) + ' * ' + str(b))
        c = a * b
    else:
        print('Question: ' + str(a) + ' - ' + str(b))
        c = a - b
    return c
