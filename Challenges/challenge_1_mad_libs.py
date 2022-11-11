"""
Ask the user to supply the words to the story in {}'s.
Tell them the story with the words they gave inserted in.
"""

# Ask the user to provide the missing words
colour = input("Give me a colour: ")
colour2 = input("Give me another colour: ")
adjective = input("And an adjective: ")


# Write a story with some words missing
story = f"""
Roses are {colour}
Violets are {colour2}
Sugar is {adjective}
And so are you
"""


# Display the final story
print(story)
