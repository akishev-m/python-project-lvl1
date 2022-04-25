import prompt

ROUNDS_COUNT = 3


# Input data: task, game
def game(task, generate_round):
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print('Hello, ' + user_name + '!\n' + task)
    round_number = 0
    while round_number < ROUNDS_COUNT:
        (question, expected_answer) = generate_round()
        print('Question: ' + question)
        answer = prompt.string('Your answer: ')
        if answer == expected_answer:
            print('Correct!')
            round_number += 1
        else:
            print('\"' + answer + '\" is wrong ;(. \
Correct answer is \"' + expected_answer + '\".')
            print('Let\'s try again, ' + user_name + '!')
            return
    print('Congratulations, ' + user_name + '!')
