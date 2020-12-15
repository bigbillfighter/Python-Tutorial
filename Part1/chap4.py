#This is chapter 4
#This chapter is mainly talking about the opeations on lists

#throughout the lists
stuffs = ['alice', 'david', 'caroline']
for stuff in stuffs:
    print(stuff.title())

print(stuff)

#use range() to output the numbers in for loop
#the numbers here includes [1,5)
for val in range(1,5):
    print(val)

#use list() to change range() to list
#lists here is number list
numbers = list(range(1,6))
print(numbers)

#use the third coefficient to control the step
for val in range(1, 11, 2):
    print(val)
even_numbers = list(range(2,11,2))
print(even_numbers)

#find the max, min, sum and other opeartions on number lists
digit=list(range(1,10))
digit.append(0)
print(digit)
print(min(digit))
print(max(digit))
print(sum(digit))

#list analysis
#be contious about the syntax that this is no colon after for loop
s_square = [value**2 for value in range(1,10)]
print(s_square)

#slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:4])
print(players[2:])
print(players[:])

#we can use negative index to point the last few elements of the list
#for example, -1 is the last number and -3 is the last but two number
print(players[-3:])
print(players[-3])

#copy the list

my_food =['pizza', 'falafel', 'carrot cake']
favourite_food = my_food[:]
print(favourite_food)

favourite_food.append('noddle')
my_food.append('hot pot')
print(favourite_food)
print(my_food)

#if just equalize the name, just to change the list favourite_food points to.
#So favourite_food is just another name of my_food. They point to the same list.
favourite_food = my_food
favourite_food.append('fish')
my_food.append('beef')
print(my_food)
print(favourite_food)

#tuple
#we use round bracket instead of square bracket to denote tuple
#elements in tuple are unchangeable
dimensions = (200, 50)
print(dimensions)
for dimension in dimensions:
    print(dimension)

#Change the values of elements in tuples is illegal. But we can change the whole tuple.
#That means the tuple variable points to another tuple.
dimensions = (300, 150)
print(dimensions)