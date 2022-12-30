from random import randint


GAME = 'What number is missing in the progression?'


MIN_NUM = 1
MAX_NUM = 50
MIN_STEP = 1
MAX_STEP = 5
MIN_LENGT = 5
MAX_LENGT = 10


def brain_ring():
    first_num = randint(MIN_NUM, MAX_NUM)
    step = randint(MIN_STEP, MAX_STEP)
    lengt_progression = randint(MIN_LENGT, MAX_LENGT)
    progression = progression_gen(first_num, step, lengt_progression)
    index = randint(0, len(progression) - 1)
    correct_answer = str(progression[index])
    progression[index] = '..'
    question = " ".join(map(str, progression))
    return question, correct_answer


def progression_gen(first_num, step, lengt_progression):
    progression = [first_num]
    while len(progression) < lengt_progression:
        progression.append(progression[-1] + step)
    return progression
