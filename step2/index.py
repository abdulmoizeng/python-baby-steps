# **********            Conditionals          ***************
# Key words : 'if', 'else', 'elif'
# Operators : ==, !=, >, >=, <, <=
# Basic example
age = 21
has_License = True
if age < 18:
    print('Don\'t drive')
else:
    print('Go drive!')

# else if ladder example
if age < 18:
    print('Don\'t drive')
elif age == 18:
    print('Start learning driving')
else:
    print('Go drive!')
# else if ladder with logical operators
# Logical operators : and, or, not
if (age < 18) and (has_License is not True):
    print('Don\'t ever think of driving!')
elif (age == 18) and (has_License is not True):
    print('Start learning driving')
elif (age == 18) and (has_License is True):
    print('You can drive on streets')
else:
    print('Go drive!')
# *****************                     *********************
