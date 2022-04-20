import random


def is_prime(num):
    index = 2
    if num == 0:
        return True
    while index <= (num / 2):
        if (num % index) == 0:
            return False
        index += 1
    return True


def prime_game_round():
    question = random.randint(0, 30)
    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'
    return str(question), answer
