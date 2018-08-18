import sys
# **********              Functions             **************
# Key words : 'def'
# Examples below


def add_number(num1, num2):
    cal = num1 + num2
    return cal


result = add_number(10, 15)
print(result)


def sub_number(num1, num2):
    return num1 - num2


result = sub_number(10, 15)
print(result)

# *****************                     ***********************

# ********** Taking cli based input from user  **************
print('What is your name?')
#name = sys.stdin.readline()
#print('Hello %s' % name)
# *****************                     *********************

# **********          More on Strings          **************
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
# *****************                     *********************
