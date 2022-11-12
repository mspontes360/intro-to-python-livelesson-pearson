"""
Guess the number between 1 and 10
"""

import random
answer = random.randint(1, 10)

guess = int(input("I'm thinking of a number between 1 and 10: "))

if guess == answer:     # If the number is correct, tell the user
    print("Congratulations!!!")
elif guess < answer:    # Otherwise, tell them if the answer is higher or lower than their guess
    print('The number chosen was less than the thinker')
else:
    print('The number chosen was greater than the thinker')

print('The number was {}'.format(answer))