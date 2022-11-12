"""
Number guessing game
The number to guess will be from 1 to 20 (inclusive).
The user will have 3 guesses to guess the number correctly.
After each wrong guess, the user will be told whether to
guess higher or lower next time.
If the user doesn't win, tell them the number.
"""
import random


def run_game():
    attempt = 1
    answer = random.randint(1, 20)
    print("I'm thinking of a number between 1 and 20")

    while attempt <= 3:
        guess = int(input(f'Attempt {attempt}! Make a guess: '))

        if guess == answer:
            print("Correct!")
            break
        else:
            if guess > answer:
                print("Nope, it's higher!")
            else:
                print("Nope. it's lower!")

        if attempt < 3:
            print('Try again\n')
        else:
            print('\nOh no!\nThe number was {}'.format(answer))

        attempt += 1


run_game()
