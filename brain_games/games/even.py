#!/usr/bin/env python

import random


def is_even(name=''):
    if name == 'TASK':
        return 'Answer "yes" if the number is even, otherwise answer "no".'
    else:
        num = round(random.random() * 10)
        print(str(num))
    return 'yes' if num % 2 == 0 else 'no'
