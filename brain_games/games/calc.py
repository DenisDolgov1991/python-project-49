from random import randint, choice


GAME = "What is the result of the expression?"


MIN_NUM = 1
MAX_NUM = 50


def calculator(num1, num2, operator):
    if operator == '+':
        correct_answer = str(num1 + num2)
    elif operator == '-':
        correct_answer = str(num1 - num2)
    else:
        correct_answer = str(num1 * num2)
    return correct_answer


def brain_ring():
    num1 = randint(MIN_NUM, MAX_NUM)
    num2 = randint(MIN_NUM, MAX_NUM)
    operator = choice('+-*')
    question = f"{num1} {operator} {num2}"
    correct_answer = str(calculator(num1, num2, operator))
    return question, correct_answer
