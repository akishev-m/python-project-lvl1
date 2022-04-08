#!/usr/bin/env python

import random


def is_even():
    question = random.randint(0, 100)
    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return str(question), answer
