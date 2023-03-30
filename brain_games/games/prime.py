from random import randint


GAME_CONDITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def calculate_the_correct_answer():
    num = randint(0, 100)
    question = str(num)
    largest_divisor_number = int(num ** 0.5)

    def is_prime(x):
        for i in range(2, largest_divisor_number + 1):
            if x % i == 0:
                break
            return x % i == 0

    correct_answer = 'no'
    if is_prime(num):
        correct_answer = 'yes'

    return question, correct_answer
