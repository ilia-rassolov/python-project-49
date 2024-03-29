from random import randint


GAME_CONDITION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(x):
    return x % 2 == 0


def calculate_correct_answer():
    num = randint(1, 99)
    question = num

    correct_answer = 'no'
    if is_even(num):
        correct_answer = 'yes'

    return question, correct_answer
