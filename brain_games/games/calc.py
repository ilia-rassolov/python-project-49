from random import randint, choice


game_condition = 'What is the result of the expression?'


def calculation_correct_answer():
    all_signs = '*+'
    sign = choice(all_signs)
    number_1 = randint(1, 10)
    number_2 = randint(1, 10)
    question = f'{number_1} {sign} {number_2}'
    correct_answer = eval(question)

    return question, str(correct_answer)
