#!/usr/bin/env python

import prompt

TOTAL_ROUNDS = 3


# Input data: task, game
def game(task, game_function):
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print('Hello, ' + user_name + '!\n' + task)
    round_number = 0
    while round_number < TOTAL_ROUNDS:
        (question, expected_answer) = game_function()
        print('Question: ' + question)
        answer = prompt.string('Your answer: ')
        if answer == expected_answer:
            print('Correct!')
            round_number += 1
        else:
            print('\"' + answer + '\" is wrong ;(. \
Correct answer is \"' + expected_answer + '\".')
            print('Let\'s try again, ' + user_name + '!')
            break
    if round_number == TOTAL_ROUNDS:
        print('Congratulations, ' + user_name + '!')
