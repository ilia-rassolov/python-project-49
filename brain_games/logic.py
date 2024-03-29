import prompt


NUMBER_OF_ROUNDS = 3


def play_game(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GAME_CONDITION)
    for i in range(NUMBER_OF_ROUNDS):
        question, correct_answer = game.calculate_correct_answer()
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
