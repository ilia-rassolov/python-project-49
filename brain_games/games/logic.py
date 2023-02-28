import prompt


def game_make(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.game_condition)
    answer_1 = prompt.string(f'Question: {game.question_1}  ')
    if answer_1 != game.correct_answer_1:
        print(f"{answer_1} is wrong answer ;(. Correct\
 answer was {game.correct_answer_1}.")
        print(f"Let's try again, {name}")
    else:
        print('Correct!')
        answer_2 = prompt.string(f'Question: {game.question_2}  ')
        if answer_2 != game.correct_answer_2:
            print(f"{answer_2} is wrong answer ;(. Correct\
 answer was {game.correct_answer_2}.")
            print(f"Let's try again, {name}")
        else:
            print('Correct!')
            answer_3 = prompt.string(f'Question: {game.question_3}  ')
            if answer_3 != game.correct_answer_3:
                print(f"{answer_3} is wrong answer ;(. Correct\
 answer was {game.correct_answer_3}.")
                print(f"Let's try again, {name}")
            else:
                print('Correct!')
                print(f'Congratulations, {name}')
