#!/usr/bin/env python

import random


def prime(name=''):
    if name == 'TASK':
        return 'Answer "yes" if given number is prime. Otherwise answer "no".'
    else:
        num = random.randint(0, 30)
        print(str(num))
        index = 2
        while index <= (num / 2):
            if (num % index) == 0 and num != 0:
                return 'no'
            index += 1
        return 'yes'
