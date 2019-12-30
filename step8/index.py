fruits_name = ['Apples', 'Bananas', 'Oranges', 'Grapes']
fruits_prices = [40, 10, 50, 12]

#print all the fruits name
print('Fruits Name', fruits_name)

#print all the fruits prices
print('Fruits Name', fruits_prices)

#print the first fruit name
print('First Fruit name', fruits_name[0])

#print the last fruit name
print('Last fruit name', fruits_name[-1])

#print the first three fruit prices
print('First three prices from the fruits list', fruits_prices[0:2])

#print the last two names from the fruits list
print('Last two names from the fruits list', fruits_name[2:])

#print the first two names from the fruits list
print('First two names from the fruits list', fruits_name[:2])

#get the multiplied of the fruit prices for the last fruit
print('Price of 2 Grapes', fruits_name[-1], fruits_prices[-1]*2)

#Change price of Orange - Lists are mutable therefore the values in the list can be changed
fruits_prices[2] = 35
print('Price of fruits',fruits_prices)

#Use of index method to get the index number Oranges price
print('Index number for Orange in the fruits price list', fruits_prices.index(35))
print('Index number for Orange in the fruits name list', fruits_name.index('Oranges'))

#Get the count of grapes
print('Count of the Grapes name in the list', fruits_name.count('Grapes'))
