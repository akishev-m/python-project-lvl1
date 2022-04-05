#!/usr/bin/env python

import random


def progression():
    start_num = random.randint(0, 100)
    step = random.randint(1, 9)
    length = random.randint(5, 15)
    mis_position = random.randint(1, length)
    question = 'Question:'
    index = 1
    while index <= length:
        if index == mis_position:
            question = question + ' ' + '..'
            exp = start_num
        else:
            question = question + ' ' + str(start_num)
        start_num += step
        index += 1
    print(question)
    return int(exp)


def main():
    progression()


if __name__ == '__main__':
    main()
