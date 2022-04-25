import random

QUESTION = 'Find the greatest common division of given numbers.'


def gcd_calculation(a, b):
    answer = 1
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
        answer = a + b
    return answer


def gcd_game_round():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    question = str(a) + ' ' + str(b)
    answer = gcd_calculation(a, b)
    return question, str(answer)
