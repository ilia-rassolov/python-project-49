import prompt
from brain_games.cli import welcome_user


def play_game(game):
    name = welcome_user()
    print(game.GAME_CONDITION)
    for i in range(3):
        question, correct_answer = game.calculation_correct_answer()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. Correct\
 answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
        print('Correct!')
    else:
        print(f'Congratulations, {name}!')
