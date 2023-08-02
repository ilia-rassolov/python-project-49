from random import randint


GAME_CONDITION = 'What number is missing in the progression?'


def generate_progression():
    first_in_sequence = randint(0, 10)
    step_sequence = randint(1, 10)
    sequence = []
    for i in range(10):
        sequence.append(str(first_in_sequence + i * step_sequence))
    return sequence


def calculate_correct_answer():
    unknown_sequence_number = randint(0, 9)
    sequence_string = generate_progression()
    correct_answer = sequence_string[unknown_sequence_number]
    sequence_string[unknown_sequence_number] = '..'
    question = ' '.join(sequence_string)

    return question, str(correct_answer)
