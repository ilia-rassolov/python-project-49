from random import randint


GAME_CONDITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def calculation_correct_answer():
    num = randint(0, 100)
    question = str(num)
    largest_divisor_number = int(num ** 0.5)
    for i in range(2, largest_divisor_number + 1):
        if num % i == 0:
            correct_answer = 'no'
            break
        else:
            correct_answer = 'yes'

    return (question, str(correct_answer))
