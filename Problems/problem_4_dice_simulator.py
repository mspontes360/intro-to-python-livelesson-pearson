"""
Randomly returns two numbers between 1 and 6
"""
import random

# Generate two random integer between 1 and 6 (inclusive)
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

# Tell the user what the result was
print("You rolled a " + str(dice1) + " and a " + str(dice2))
