#!/usr/bin/env python

import random


def calc():
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    opperation = random.randint(1, 3)
    answer = None
    if opperation == 1:
        question = str(a) + ' + ' + str(b)
        answer = a + b
    elif opperation == 2:
        question = str(a) + ' * ' + str(b)
        answer = a * b
    else:
        question = str(a) + ' - ' + str(b)
        answer = a - b
    return question, answer
