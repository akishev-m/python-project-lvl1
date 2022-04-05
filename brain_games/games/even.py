#!/usr/bin/env python

import random


def is_even():
    num = round(random.random() * 10)
    print('Question: ' + str(num))
    return 'yes' if num % 2 == 0 else 'no'
