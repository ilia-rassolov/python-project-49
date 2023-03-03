from random import randint


game_condition = 'What number is missing in the progression?'

first_in_sequence_1 = randint(0, 10)
step_sequence_1 = randint(1, 10)
unknown_sequence_number_1 = randint(0, 9)
sequence_1 = []
for i in range(10):
    sequence_1.append(first_in_sequence_1 + i * step_sequence_1)
result_1 = sequence_1[unknown_sequence_number_1]
correct_answer_1 = str(result_1)
sequence_1.pop(unknown_sequence_number_1)
sequence_1_string = map(str, sequence_1)
sequence_1.insert(unknown_sequence_number_1, '..')
question_1 = ' '.join(sequence_1_string)

first_in_sequence_2 = randint(0, 10)
step_sequence_2 = randint(1, 10)
unknown_sequence_number_2 = randint(0, 9)
sequence_2 = []
for i in range(10):
    sequence_2.append(first_in_sequence_2 + i * step_sequence_2)
result_2 = sequence_2[unknown_sequence_number_2]
correct_answer_2 = str(result_2)
sequence_2.pop(unknown_sequence_number_2)
sequence_2.insert(unknown_sequence_number_2, '..')
sequence_2_string = map(str, sequence_2)
question_2 = ' '.join(sequence_2_string)

first_in_sequence_3 = randint(0, 10)
step_sequence_3 = randint(1, 10)
unknown_sequence_number_3 = randint(0, 9)
sequence_3 = []
for i in range(10):
    sequence_3.append(first_in_sequence_3 + i * step_sequence_3)
result_3 = sequence_3[unknown_sequence_number_3]
correct_answer_3 = str(result_3)
sequence_3.pop(unknown_sequence_number_3)
sequence_3.insert(unknown_sequence_number_3, '..')
sequence_3_string = map(str, sequence_3)
question_3 = ' '.join(sequence_3_string)
