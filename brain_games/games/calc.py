import random

QUESTION = 'What is the result of the expression?'
ADDITION = '+'
SUBSTRACTION = '-'
MULTIPLICATION = '*'


def generate_calc_round():
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    operation = random.choice((ADDITION, SUBSTRACTION, MULTIPLICATION))
    question = str(a) + ' ' + operation + ' ' + str(b)
    if operation == ADDITION:
        answer = a + b
    elif operation == SUBSTRACTION:
        answer = a - b
    elif operation == MULTIPLICATION:
        answer = a * b
    else:
        raise Exception("Error")
    return question, str(answer)
