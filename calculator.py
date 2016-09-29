"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here

while True: 

	user_input = raw_input('>: ')
	tokens = user_input.split(' ')
	
	if tokens[0] == '+':
		print reduce(add, tokens[1:])

	if tokens[0] == '-':
		print subtract(int(tokens[1]), int(tokens[2]))

	if tokens[0] == '*':
		print multiply(int(tokens[1]), int(tokens[2]))

	if tokens[0] == '/':
		print divide(int(tokens[1]), int(tokens[2]))

	if tokens[0] == 'square':
		print square(int(tokens[1]), int(tokens[2]))

	if tokens[0] == 'cube':
		print cube(int(tokens[1]))

	if tokens[0] == 'pow':
		print power(int(tokens[1]), int(tokens[2]))

	if tokens[0] == '%':
		print mod(int(tokens[1]), int(tokens[2]))

	if tokens[0] == 'q':

		break