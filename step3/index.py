# Loops
# Key words : 'for', 'while'

import random

# for loop:

for x in range(0, 10):
    print(x)

print('\n')

grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
for y in grocery_list:
    print(y)

print('\n')

for x in [2, 4, 6, 8, 10]:
    print(x)

print('\n')

num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]
for x in range(0, 3):
    for y in range(0, 3):
        print(num_list[x][y])

# While loop:

random_num = random.randrange(0, 100)
while random_num is not 15:
    print(random_num)
    random_num = random.randrange(0, 100)

i = 0
while i <= 20:
    if i % 2 == 0:
        print(i)
    elif i == 9:
        break
    else:
        i += 1
        continue
    i += 1
