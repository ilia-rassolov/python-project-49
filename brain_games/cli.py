import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    global name
    print(f'Hello, {name}!')


name = prompt.string('May I have your name? ')
