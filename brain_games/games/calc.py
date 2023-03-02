from random import randint, choice


game_condition = 'What is the result of the expression?'
sign = '*+'
question_1 = str(randint(1, 10)) +\
' ' + str(choice(sign)) + ' ' + str(randint(1, 10))
result_1 = eval(question_1)
correct_answer_1 = str(result_1)
question_2 = str(randint(1, 10)) +\
' ' + str(choice(sign)) + ' ' + str(randint(1, 10))
result_2 = eval(question_2)
correct_answer_2 = str(result_2)
question_3 = str(randint(1, 10)) +\
' ' + str(choice(sign)) + ' ' + str(randint(1, 10))
result_3 = eval(question_3)
correct_answer_3 = str(result_3)
