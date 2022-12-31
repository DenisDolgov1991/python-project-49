from random import randint
import math


GAME = 'Find the greatest common divisor of given numbers.'


MIN_NUM = 1
MAX_NUM = 50


def brain_ring():
    num1 = randint(MIN_NUM, MAX_NUM)
    num2 = randint(MIN_NUM, MAX_NUM)
    question = f'{num1} {num2}'
    correct_answer = str(math.gcd(num1, num2))
    return question, correct_answer
