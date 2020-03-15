## Solutions to Fun Challenges with Python baby steps: 

##### Boolean Practice with Python :
```
True
False
False
True
True
True
False
True
False
False
False
False
True
False
False
False
True
True
False
False
```

##### Squaring numbers in python : 
```
# Defining a list with 10 numbers

numbers_to_be_squared = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Defining a `for` loop to square each item of the list

for number in numbers_to_be_squared:
    print(f"The square of the number {number} is {number * number}")
    # Additional point for ** sign
    print(f"The square of the number {number} is {number ** 2}")

# Additional Point : If the list [numbers] is not defined that could be replaced by list(range(1,11))

for number in list(range(1, 11)):
    print(f"Thw square of {number} is {number ** 2}")
```

##### Strings Case functions :
```
def upperCase(text):
    return text.upper()

def lowerCase(text):
    return text.lower()

def reverse(text):
    return text[::-1]

def upperCase_and_reverse(text):
    #Chaining both in one line
    return text.upper()[::-1]

def lowerCase_and_reverse(text):
    return text.lower()[::-1]

# Additional Points
def _upperCase_and_reverse_(text):
    upperCasedText = upperCase(text)
    reversedText = reverse(upperCasedText)
    return(reversedText)

def _lowerCase_and_reverse_(text):
    lowerCasedText = lowerCase(text)
    reversedText = reverse(lowerCasedText)
    return(reversedText)

# Calling the Defined Functions
print(f"Calling upperCase() {upperCase('Hello World!')}")
print(f"Calling lowerCase() {lowerCase('HELLO WORLD!')}")
print(f"Calling reverse() ", reverse("Hello World!"))
print(f"Calling uppercase_and_reverse() {upperCase_and_reverse('Hello World!')}")
print(f"Calling lowercase_and_reverse() ", lowerCase_and_reverse("Hello World!"))
print(f"Calling _uppercase_and_reverse_() {_upperCase_and_reverse_('Hello World!')}")
print(f"Calling _lowercase_and_reverse_()", _lowerCase_and_reverse_('Hello World!'))
```

##### Random Selector :
```
# Importing random
import random

# Defining a list for my favourite films & TV shows
my_favourite_films = ["Frozen 2", "Frozen", "The Girl Next Door", "Friends"]

# Using append to add a film to the list
my_favourite_films.append("Mary Poppins Returns")

# Using insert to define the position of the item to be inserted in the list
my_favourite_films.insert(3, "To all the boys i've loved")

# Using random to select a random item from the my_favourite_films
random_film = random.choice(my_favourite_films)

# Printing random_film
print(f"How about watching: {random_film}")

# To execute it: python3 randomSelector.py
# Response: How about watching: [random item from my_favourinte_films]
```

