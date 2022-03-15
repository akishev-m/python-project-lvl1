#!/usr/bin/env python

import prompt

def welcome_user():
    name = ''
    while name == '':
        name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')


def main():
    print("Welcome to the Brain Games!") 

if __name__ == '__main__':
    main()

