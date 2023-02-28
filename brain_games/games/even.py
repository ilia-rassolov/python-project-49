import prompt
from random import randint


def even_test():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    num1 = randint(1, 99)
    answer1 = prompt.string(f'Question: {num1} ')
    if num1 % 2 == 0:
        correct_answer1 = 'yes'
    else:
        correct_answer1 = 'no'
    if answer1 != correct_answer1:
        print(f"{answer1} is wrong answer ;(. Correct\
 answer was {correct_answer1}.")
        print(f"Let's try again, {name}")
    else:
        print('Correct!')
        num2 = randint(1, 99)
        answer2 = prompt.string(f'Question: {num2} ')
        if num2 % 2 == 0:
            correct_answer2 = 'yes'
        else:
            correct_answer2 = 'no'
        if answer2 != correct_answer2:
            print(f"{answer2} is wrong answer ;(. Correct\
 answer was {correct_answer2}.")
            print(f"Let's try again, {name}")
        else:
            print('Correct!')
            num3 = randint(1, 99)
            answer3 = prompt.string(f'Question: {num3} ')
            if num3 % 2 == 0:
                correct_answer3 = 'yes'
            else:
                correct_answer3 = 'no'
            if answer3 != correct_answer3:
                print(f"{answer3} is wrong answer ;(. Correct\
 answer was {correct_answer3}.")
                print(f"Let's try again, {name}")
            else:
                print('Correct!')
                print(f'Congratulations, {name}')
