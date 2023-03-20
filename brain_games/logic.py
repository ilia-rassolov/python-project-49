import prompt
from brain_games.cli import welcome_user, name


def play_game(game):
    welcome_user()
    print(game.game_condition)
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
