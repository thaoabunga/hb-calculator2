"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here

def convert2ints(number_strings):
    """takes in a list of numbers_strings returns a list of integers."""
    ints = []

    for number in number_strings:
        ints.append(int(number))

    return ints

while True: 

    user_input = raw_input('>: ')
    tokens = user_input.split(' ') # returns a list of strings, not integers
    number_strings = tokens[1:]

    numbers = convert2ints(number_strings)

    if tokens[0] == '+':
        print reduce(add,numbers)

    # if tokens[0] == '-':
    #     print reduce(subtract, int(tokens[1:]))

    # if tokens[0] == '*':
    #     print multiply(int(tokens[1]), int(tokens[2]))

    # if tokens[0] == '/':
    #     print divide(int(tokens[1]), int(tokens[2]))

    # if tokens[0] == 'square':
    #     print square(int(tokens[1]), int(tokens[2]))

    # if tokens[0] == 'cube':
    #     print cube(int(tokens[1]))

    # if tokens[0] == 'pow':
    #     print power(int(tokens[1]), int(tokens[2]))

    # if tokens[0] == '%':
    #     print mod(int(tokens[1]), int(tokens[2]))

    # if tokens[0] == 'q':

    #     break