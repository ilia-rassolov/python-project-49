import prompt


def play_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.game_condition)
    for i in range(3):
        question, correct_answer = game.calculation_correct_answer()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. Correct\
 answer was '{correct_answer}'.")
            print(f"Let's try again, {name}")
            break
        print('Correct!')
    else:
        print(f'Congratulations, {name}!')
