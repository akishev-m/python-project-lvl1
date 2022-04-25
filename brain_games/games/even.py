import random

QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def even_game_round():
    question = random.randint(0, 100)
    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return str(question), answer
