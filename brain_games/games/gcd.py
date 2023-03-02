from math import gcd
from random import randint


game_condition = 'Find the greatest common divisor of given numbers.'

first_in_question_1 = 5 * randint(1, 20)
second_in_question_1 = 5 * randint(1, 20)
question_1 = f'{first_in_question_1} {second_in_question_1}'
result_1 = gcd(first_in_question_1, second_in_question_1)
correct_answer_1 = str(result_1)

first_in_question_2 = 4 * randint(1, 20)
second_in_question_2 = 4 * randint(1, 20)
question_2 = f'{first_in_question_2} {second_in_question_2}'
result_2 = gcd(first_in_question_2, second_in_question_2)
correct_answer_2 = str(result_2)

first_in_question_3 = 3 * randint(1, 20)
second_in_question_3 = 3 * randint(1, 20)
question_3 = f'{first_in_question_3} {second_in_question_3}'
result_3 = gcd(first_in_question_3, second_in_question_3)
correct_answer_3 = str(result_3)
