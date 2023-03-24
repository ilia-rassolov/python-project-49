from random import randint


GAME_CONDITION = 'Answer "yes" if the number is even, otherwise answer "no".'


def calculate_the_correct_answer():
    num = randint(1, 99)
    question = num
    if num % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, str(correct_answer)
