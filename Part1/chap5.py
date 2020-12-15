#if-else syntax
car = 'Audi'
if car=='bmw':
    print(car=='bmw')
else:
    print(car=='bmw')

#use 'and' or 'or' to cpntrol the condition
a = 12
b = 21
print(a>10 and b>20)
print(a<2 or (b<11))

#use 'in' or 'not in' to tell if there is the specific value
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('tomato' in requested_toppings)
print('potato' not in requested_toppings)

a = True
print('a:'+str(a))

#if-elif-else syntax

a = 12
if a<10:
    print('a is less than 10')
elif a<20:
    print('a is less than 20 but bigger than 10')
else:
    print('a is bigger than 20')

b = []
print(b)

#in python, empty list is equal to False
if b:
    print('b is not empty!')
else:
    print('b is empty!\n')

available_toppings = ('mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese')
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")
