import random


def progression_game_round():
    start_num = random.randint(0, 100)
    step = random.randint(1, 9)
    length = random.randint(5, 15)
    missed_position = random.randint(1, length)
    question = ''
    index = 1
    while index <= length:
        if index == missed_position:
            question = question + '.. '
            answer = start_num
        else:
            question = question + str(start_num) + ' '
        start_num += step
        index += 1
    return question, str(answer)
