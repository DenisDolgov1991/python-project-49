import prompt


def game_start(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GAME)

    for _ in range(3):
        question, correct_answer = game.brain_ring()
        print(f"Question: {question}")
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct')
        else:
            print(f"""'{answer}' is wrong answer ;(.
Correct answer was '{correct_answer}'.
Let's try again, {name}!""")
            break
    print(f'Congratulations, {name}!')
