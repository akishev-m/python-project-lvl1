#!/usr/bin/env python

import random


def calc(name=''):
    if name == 'TASK':
        return 'Answer the question'
    else:
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        opperation = random.randint(1, 3)
        c = None
        if opperation == 1:
            print(str(a) + ' + ' + str(b))
            c = a + b
        elif opperation == 2:
            print(str(a) + ' * ' + str(b))
            c = a * b
        else:
            print(str(a) + ' - ' + str(b))
            c = a - b
        return c
