#!/usr/bin/env python

import random


def gcd(name=''):
    if name == 'TASK':
        return 'Find the greatest common division of given numbers.'
    else:
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        print(str(a) + ' ' + str(b))
        exp = None
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
            exp = a + b
        return exp
