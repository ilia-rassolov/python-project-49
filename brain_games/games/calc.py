from random import randint, choice
from operator import mul, add, sub


GAME_CONDITION = 'What is the result of the expression?'


def calculate_the_correct_answer():
    all_signs = '*+-'
    sign = choice(all_signs)
    number_1 = randint(1, 10)
    number_2 = randint(1, 10)
    question = f'{number_1} {sign} {number_2}'
    if sign == '*':
        correct_answer = mul(number_1, number_2)
    elif sign == '+':
        correct_answer = add(number_1, number_2)
    else:
        correct_answer = sub(number_1, number_2)

    return (question, str(correct_answer))
