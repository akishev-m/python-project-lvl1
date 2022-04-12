### Hexlet tests and linter status:
[![Actions Status](https://github.com/akishev-m/python-project-lvl1/workflows/hexlet-check/badge.svg)](https://github.com/akishev-m/python-project-lvl1/actions)
### Maintainability badge
[![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/akishev-m/python-project-lvl1)
### linter workflow badge
![linter](https://github.com/akishev-m/python-project-lvl1/actions/workflows/github-lint.yml/badge.svg)

### Project description
 Brain-game is a command line game, that suggest users to answer a mathematical questions depnds on game type. There are 5 types of games, that could be started by relevant command in terminal: brain-calc, brain-even, brain-prime, brain-gcd, brain-progression. Every game asks user name and output the question. If user input correct answers three times in a row, game output congratulation words and ends. In a case of incorrect answer, the game output correct answer and also ends.

Game launched by relevand command that execute relevant script in '/brain\_games/scripts'. Scripts use 'game\_engine.py' and modules in '/brain\_games/games' to start the game. Description of game types you could see below in 'Usage' section.

### SYSTEM REQUIREMENTS: 
Operating system: Ubuntu 20.04
Python 3.8

### Installation
to build a package use 'make build' or 'poetry build'
to install package use 'make package-install' or 'python3 -m pip install --user dist/\*.whl

### Usage
Start the game by using one of the following commands.

brain-calc: game suggest to calculate sum, multiplication or deduction of two numbers
brain-even: game output the number and ask if the number is even
brain-prime: game output the number and ask if the number is prime
brain-gcd: game output two numbers and propose to find the greatest common divisor 
brain-progression: game output number sequence of arithmetic progression with one missing number and suggest to find missed number

game demonstration: https://asciinema.org/a/SYHaSv6UQkUVPdxkFFddnUEZy

### Development steps

Step 1 (welcome words)
https://asciinema.org/a/18x9XKXT4esVS2NDLoUvkrnW4

Step 2 (build and install packages)
https://asciinema.org/a/SP5Z0EqMm8OJNoNGIX20EboKj

Step 3 (add prompt, publish changes)
https://asciinema.org/a/S3OU6CFtKSiSCvNe8XaIzUy3y

Step 4 (make lin)
https://asciinema.org/a/nHeEjapt4sm0QcTOeWVP4x2x6

Step 5 (Even)
https://asciinema.org/a/87z0gsCclDyYfVndBmjmkUQHO

Step 6 (Calc)
https://asciinema.org/a/qycPsuF75WdX0Fl2ZWSTgrO8g

Step 7 (Greatest common division)
https://asciinema.org/a/44Y3sWWKCNCWClipd1DIr3QBI

Step 8 (progression)
https://asciinema.org/a/ctqc0lAxrBphBmbYZV0tAbI8u

Step 9 (Prime)
https://asciinema.org/a/vwgNn13POYhi8U9GMrtNn3WrV


