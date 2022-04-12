#!/usr/bin/env python

import random


def calc():
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    opperation = random.choice(('-', '+', '*'))
    question = str(a) + ' ' + opperation + ' ' + str(b)
    answer = eval(question)
    return question, answer
