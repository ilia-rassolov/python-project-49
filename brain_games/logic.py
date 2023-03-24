import prompt
from brain_games.cli import welcome_user


def play_game(game):
    NUMBER_OF_ROUNDS = 3
    name = welcome_user()
    print(game.GAME_CONDITION)
    for i in range(NUMBER_OF_ROUNDS):
        question, correct_answer = game.calculate_the_correct_answer()
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
