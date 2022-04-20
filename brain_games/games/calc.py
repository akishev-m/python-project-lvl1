import random


def calc_game_round():
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    opperation = random.choice(('-', '+', '*'))
    question = str(a) + ' ' + opperation + ' ' + str(b)
    if opperation == '-':
        answer = a - b
    elif opperation == '+':
        answer = a + b
    else:
        answer = a * b
    return question, str(answer)
