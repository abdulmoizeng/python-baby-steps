# Traditional Hello World! Starter !!
print("Hello World!")

# Comments in Python
# This is a single line comment by using `#`
# Multiline comments can be implemented by using `"""`

"""
Multi line comments
    This is a Multiline comment
"""

# Variable declaration in python

"""
The Rules
    Variables names must start with a letter or an underscore, such as:
        - _underscore
        - underscore_
        The remainder of your variable name may consist of letters, numbers and underscores.
        - password1
        - n00b
        - un_der_scores
"""

name = "Muhammad AbdulMoiz"
print("My name is %s . I am a Software Developer at %s" % (name, "Sastaticket.Pk"))

# Data types in python
# Numbers | String | Lists | Tuples | Dictionaries

# Data type Numbers basic examples:

number1 = 10  # This is a number
float_num = 10.2  # This is a float
print("Number : %d . float_num %f" % (number1, float_num))
print("Number", number1, "  Float number : ", float_num)

# Data type String basic examples :
quote = "\" keep doing cool stuff "
# ^  It covers example of using quotes in string `"`
multiline_quote = """
                    Its a multi line quote
                    line 1
                    line 2
                    ...
                    ...
                    ...
                    line x
                  """
print("We should always %s" % quote)
print("Example of multi line quotes %s" % multiline_quote)
print('\n' * 5)  # it will print new line 5 times in console

# Data type Lists basic examples:
grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
grocery_list[0] = 'Fresh Juice'
print(grocery_list[1:3])  # From index: 1 till 3rd item

other_events = ['Wash Car', 'Pick Up Kids', 'Cash Check']
to_do_list = [grocery_list, other_events]  # make 2 dimensional array
to_do_list2 = grocery_list + other_events  # concatenate two arrays
print(to_do_list[1][1])

grocery_list.append('Onions')  # => ['Juice', 'Tomatoes', 'Potatoes', 'Bananas', 'Onions]
grocery_list.insert(1, 'Pickle')  # => ['Juice', 'Pickle', 'Tomatoes', 'Potatoes', 'Bananas', 'Onions]
grocery_list.remove('Pickle')  # => ['Juice', 'Tomatoes', 'Potatoes', 'Bananas', 'Onions]
grocery_list.sort()
grocery_list.reverse()

print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))

# Data type Tuples basic examples:

# Tuples are similar to a List but they are immutable
pi_tuple = (3, 1, 4, 1, 5, 9)
new_list = list(pi_tuple)
new_tuple = tuple(new_list)
len(pi_tuple)
max(pi_tuple)
min(pi_tuple)
nested_tuple = ('A', (1, 2), 'B', ('a', 'b'))
print(nested_tuple[1])  # (1,2)
social_profiles = (
    ('Twitter', 'data'),
    ('Facebook', 'data'),
    ('Google', 'data')
)
print(dict(social_profiles))  # we can only convert length 2 tuple into direct dictionary
social_profiles = (
    ('Twitter', 'data1', 'data2'),
    ('Facebook', 'data1', 'data2', 'data3'),
    ('Google', 'data1', 'data2', 'data3', '.....')
)
# ^ Converting above to dictionary will generate error, following is the right way to structure this data 
social_profiles = (
    ('Twitter', ['data1', 'data2']),
    ('Facebook', ['data1', 'data2', 'data3']),
    ('Google', ['data1', 'data2', 'data3', '.....'])
)
print(dict(social_profiles))  # converting tuple to dictionary

# Data type Dictionary basic examples:
# Dictionaries are values with unique keys
super_villains = {
    'Fiddler': 'Issac Bowin',
    'Captain Cold': 'Leonard Snart',
    'Weather Wizard': 'Mark Mardon',
    'Pied Piper': 'Thomas Peterson'
}

del super_villains['Fiddler']
print(len(super_villains))
print(super_villains.get('Pied Piper'))
print(super_villains.keys())
print(super_villains.values())