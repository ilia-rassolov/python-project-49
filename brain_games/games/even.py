from random import randint


game_condition = 'Answer "yes" if the number is even, otherwise answer "no".'


def calculation_correct_answer():
    num = randint(1, 99)
    question = num
    if num % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, str(correct_answer)
