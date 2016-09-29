def add(num1, num2):
    return int(num1) + int(num2)


def subtract(num1, num2, num3 ='1'):
    return num1 - num2 - num3


def multiply(num1, num2, num3 ='1'):
    return num1 * num2 * num3


def divide(num1, num2, num3 ='1'):
    # Need to turn at least argument to float for division to
    # not be integer division
    return float(num1) / float(num2) / float(num3) 


def square(num1):
    # Needs only one argument
    return num1 * num1 


def cube(num1):
    # Needs only one argument
    return num1 * num1 * num1


def power(num1, num2):
    return num1 ** num2  # ** = exponent operator


def mod(num1, num2):
    return num1 % num2
