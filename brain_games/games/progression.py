from random import randint


game_condition = 'What number is missing in the progression?'


def calculation_correct_answer():
    first_in_sequence = randint(0, 10)
    step_sequence = randint(1, 10)
    unknown_sequence_number = randint(0, 9)
    sequence = []
    for i in range(10):
        sequence.append(first_in_sequence + i * step_sequence)
    correct_answer = sequence[unknown_sequence_number]
    sequence.pop(unknown_sequence_number)
    sequence_string = map(str, sequence)
    sequence.insert(unknown_sequence_number, '..')
    question = ' '.join(sequence_string)

    return question, str(correct_answer)
