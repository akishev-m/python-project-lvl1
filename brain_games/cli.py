#!/usr/bin/env python

import prompt

def welcome_user():
    name = ''
    while name == '':
        name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')

def main():
    welcome_user()

if __name__ == '__main__':
    main()

