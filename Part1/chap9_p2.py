#the python library practise
from collections import OrderedDict

favourite_languages = OrderedDict()

favourite_languages['Lily'] = 'C'
favourite_languages['Max'] = 'Ruby'
favourite_languages['Lucas'] = 'Java'
favourite_languages['Peter'] = 'C'

for name, language in favourite_languages.items():
    print(name.title()+"'s favourite language is "+language.title())


#random library includes the meethods that generate random numbers
#for example, randint(a, b) can return an integer that between a and b

from random import randint
num = list(range(1, 7))
for i in range(1,10000):
    x = randint(1,6)
    num[x-1]+=1
print(num)

#when we define classes, we let all the first letters capital instead of using '_'
#like what we do on functions
#for example: class MyFavouriteFood():
#def get_my_favourite_food(self):