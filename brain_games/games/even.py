from random import randint


GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


MIN_NUM = 1
MAX_NUM = 50


def is_even(num):
    return num % 2 == 0


def brain_ring():
    num = randint(MIN_NUM, MAX_NUM)
    question = str(num)
    correct_answer = 'yes' if is_even(num) else 'no'
    return question, correct_answer
