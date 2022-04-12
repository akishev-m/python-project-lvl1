#!/usr/bin/env python

import random


def gcd_calculation(a, b):
    answer = ''
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
        answer = a + b
    return answer


def gcd():
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    question = str(a) + ' ' + str(b)
    answer = gcd_calculation(a, b)
    return question, answer
