import prompt
from randome import randit
from cli import welcome_user


def even_numbers():
    welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    num1 = randit(1, 99)
    answer1 = prompt.string('Question: {num1}')
    if num1 % 2 == 0:
        correct_answer1 = 'yes'
    else:
         correct_answer1 = 'no'
    if answer1 != correct_answer1:
        print(f"{answer1} is wrong answer ;(. Correct answer was {correct_answer1}.")
        print(f"Let's try again, {name}")
    print('Correct!')
    num2 = randit(1, 99)
    answer2 = prompt.string('Question: {num2}')
    if num2 % 2 == 0:
        correct_answer2 = 'yes'
    else:
        correct_answer2 = 'no'
    if answer2 != correct_answer2:
        print(f"{answer2} is wrong answer ;(. Correct answer was {correct_answer2}.")
        print(f"Let's try again, {name}")
    print('Correct!')
    num3 = randit(1, 99)
    answer3 = prompt.string('Question: {num3}')
    if num3 % 2 == 0:
        correct_answer3 = 'yes'
    else:
        correct_answer3 = 'no'
    if answer3 != correct_answer3:
        print(f"{answer3} is wrong answer ;(. Correct answer was {correct_answer3}.")
        print(f"Let's try again, {name}")
    print('Correct!')
    print(f'Congratulations, {name}')
