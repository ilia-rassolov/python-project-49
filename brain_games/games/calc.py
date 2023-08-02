from random import randint, choice
from operator import mul, add, sub


GAME_CONDITION = 'What is the result of the expression?'


def calculate_correct_answer():
    all_signs = '*+-'
    sign = choice(all_signs)
    number_1 = randint(1, 10)
    number_2 = randint(1, 10)
    question = f'{number_1} {sign} {number_2}'

    def define_operator(x, y):
        if sign == '*':
            return mul(x, y)
        elif sign == '+':
            return add(x, y)
        else:
            return sub(x, y)

    correct_answer = define_operator(number_1, number_2)

    return question, str(correct_answer)
