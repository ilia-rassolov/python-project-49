from math import gcd
from random import randint


game_condition = 'Find the greatest common divisor of given numbers.'


def calculation_correct_answer():
    first_in_question = 5 * randint(1, 20)
    second_in_question = 5 * randint(1, 20)
    question = f'{first_in_question} {second_in_question}'
    result = gcd(first_in_question, second_in_question)
    correct_answer = str(result)

    return question, str(correct_answer)
