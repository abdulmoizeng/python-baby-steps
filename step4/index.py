# Functions
# Key words : 'def'

import sys


# Example
def add_number(num1, num2):
    cal = num1 + num2
    return cal


result = add_number(10, 15)
print(result)


def sub_number(num1, num2):
    return num1 - num2


result = sub_number(10, 15)
print(result)


def sum(num1, num2, num3):
    return num1 + num2 + num3


args = (1, 2, 3)  # usually a tuple, always an iterable[1]
# The *args argument is called the "variable positional parameter"
print(sum(*args))  # -> sum(1, 2, 3)

# kwargs is the "variable keyword parameter
kwargs = {"num1": 1, "num2": 2, "num3": 3}  # usually a dict, always a mapping*

print(sum(**kwargs))  # -> sum(1, 2, 3)

# Taking cli based input from user

print('What is your name?')

# name = sys.stdin.readline()
# print('Hello %s' % name)

# More on Strings :
some_str = ' i\'ll catch the bus! '
print(some_str[0:4])
print(some_str[-5:])
print(some_str[:-5])
print(some_str[0:4] + " be there")
print(some_str.capitalize())
print(some_str.find('bus'))
print(some_str.find('Bus'))
print(some_str.isalpha())
print(some_str.isalnum())
str1 = "this2009"  # No space in this string
str2 = "this"  # No space & digit in this string
print(str2.isalpha())
print(str1.isalnum())
print(some_str.replace('bus', 'plane'))
print(some_str.strip())  # remove white space
print(some_str.split())  # split into a list of words => ["i'll", 'catch', 'the', 'bus!']


# Lambda Functions :

def lfunc(a):
    # lambda argument : expression
    return lambda c: c * a


# using a lambda function to double and triple.
myDoubler = lfunc(2)
myTripler = lfunc(3)

# invoking the function
print("Doubling 2 :", myDoubler(2))
print("Tripling 2 :", myTripler(2))
