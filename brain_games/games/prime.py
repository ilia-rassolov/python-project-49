from random import randint


game_condition = 'Answer "yes" if given number is prime. Otherwise answer "no"'

number_1 = randint(0, 100)
question_1 = number_1
largest_divisor_number_1 = int(number_1 ** 0.5)
for i in range(2, largest_divisor_number_1 + 1):
    if number_1 % i == 0:
        correct_answer_1 = 'no'
        break
    else:
        correct_answer_1 = 'yes'

number_2 = randint(0, 100)
question_2 = number_2
largest_divisor_number_2 = int(number_1 ** 0.5)
for i in range(2, largest_divisor_number_2 + 1):
    if number_2 % i == 0:
        correct_answer_2 = 'no'
        break
    else:
        correct_answer_2 = 'yes'

number_3 = randint(0, 100)
question_3 = number_3
largest_divisor_number_3 = int(number_1 ** 0.5)
for i in range(2, largest_divisor_number_3 + 1):
    if number_3 % i == 0:
        correct_answer_3 = 'no'
        break
    else:
        correct_answer_3 = 'yes'