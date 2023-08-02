from random import randint


GAME_CONDITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(x):
    largest_divisor_number = int(x ** 0.5)
    for i in range(2, largest_divisor_number + 1):
        if x % i == 0:
            return True
    return False


def calculate_correct_answer():
    num = randint(0, 100)
    question = str(num)

    if is_prime(num):
        correct_answer = 'no'
    else:
        correct_answer = 'yes'

    return question, correct_answer
