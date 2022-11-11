"""
Fill out the functions to calculate the area and circumference of a circle.
Print the result to the user.
"""
import math


def area(r):
    return math.pi * r ** 2


def circumference(r):
    return math.pi * 2 * r


radius = float(input("Circle radius: "))

print(f'Area: {area(radius)}')  # <-- Call the area function and print the result
print(f'Circumference: {circumference(radius)}')  # <-- Call the circumference function and print
