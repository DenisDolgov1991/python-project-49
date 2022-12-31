from random import randint


GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


MIN_NUM = 1
MAX_NUM = 50


def brain_ring():
    num = randint(MIN_NUM, MAX_NUM)
    question = str(num)
    if is_prime(num):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
