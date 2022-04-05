#!/usr/bin/env python

import random


def calc():
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    opperation = random.randint(1, 3)
    c = None
    if opperation == 1:
        print('Question: ' + str(a) + ' + ' + str(b))
        c = a + b
    elif opperation == 2:
        print('Question: ' + str(a) + ' * ' + str(b))
        c = a * b
    else:
        print('Question: ' + str(a) + ' - ' + str(b))
        c = a - b
    return c
