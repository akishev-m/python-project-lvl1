#!/usr/bin/env python

import random


def prime():
    num = random.randint(0, 30)
    print('Question: ' + str(num))
    index = 2
    while index <= (num / 2):
        if (num % index) == 0 and num != 0:
            return 'no'
        index += 1
    return 'yes'
