#!/usr/bin/env python

import prompt

NUMBER_OF_QUESTIONS = 3


# Compare user answer with expected and show relevant message
def is_correct(answer, expected_answer, user_name):
    if str(answer) == str(expected_answer):
        print('Correct!')
        return True
    else:
        print('\"' + str(answer) + '\" is wrong ;(. \
Correct answer is \"' + str(expected_answer) + '\".')
        print('Let\'s try again, ' + user_name + '!')
        return False


# Input data: task, game
def game(task, game_function):
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print('Hello, ' + user_name + '!\n' + task)
    question_number = 0
    while question_number < NUMBER_OF_QUESTIONS:
        (question, expected_answer) = game_function()
        print('Question: ' + question)
        answer = prompt.string('Your answer: ')
        if is_correct(answer, expected_answer, user_name):
            question_number += 1
        else:
            break
    if question_number == NUMBER_OF_QUESTIONS:
        print('Congratulations, ' + user_name + '!')
