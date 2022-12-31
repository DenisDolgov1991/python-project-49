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
    i = 0
    for n in range(2, num // 2 + 1):
        if num % n == 0:
            i += 1
    if i > 0:
        return False
    else:
        return True
