#dictionary
#the relationships between keys and values are 1:n
#we can store almost any data in dictionary

#example
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

alien_0['x_position'] = 255
alien_0['y_position'] = 0
print(alien_0)

#the order of key-value couples doesn't make sense
#That means there is no order in key-value couples like set

alien_0['color'] = 'yellow'
print(alien_0)

#delete the key-value couple
del alien_0['x_position']
print(alien_0)

#throughout the dictionary
user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}
for key, value in user_0.items():
    print('\nKey: '+key)
    print('Value: '+value)

print()

#key attribute
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

for name in favorite_languages.keys():
    print(name.title())
print()

#At default, if we didn't point to any attribute, the console will ouput the keys
for name in favorite_languages:
    print(name.title())

#the keys attribute will return a list with all of the keys
print(favorite_languages)
print(favorite_languages.keys())

#output the elements in the dictionatry sorted
print(sorted(favorite_languages.keys()))

#use values attribute to output the values
print()
for language in favorite_languages.values():
    print(language)

#use set method to remove the duplicated values
print('\nThe following languages are mentioned!')
for language in set(favorite_languages.values()):
    print(language)

#you can nest list with dict or dict with nest
alien_0 = {'color': 'yellow', 'points': 5}
alien_1 = {'color': 'green', 'points': 3}
alien_2 = {'color': 'black', 'points': 10}
alien_3 = {'color': 'yellow', 'points': 2}

aliens = [alien_0, alien_1, alien_2, alien_3]
for alien in aliens:
    print(alien)

#use loop to generate aliens automatically
aliens = []
#use one coefficient can control the times the loop has
for alien_num in range(30):
    new_alien = {'color': 'green', 'point': 5}
    aliens.append(new_alien)
#print(aliens)
for alien in aliens[:5]:
    print(alien)
print('......')

#nest dict with list
pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}

print(pizza)
print(pizza['toppings'])

print('The pizza is with '+pizza['crust']+' crust')
print('The toppings are:')
for topping in pizza['toppings']:
    print(topping)

favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}

for name in favorite_languages.keys():
    if len(favorite_languages[name])==1:
        print('\n'+name.title()+"'s favourite is:")
    else:
        print('\n'+name.title()+"'s favourite are:")
    for lan in favorite_languages[name]:
        print(lan.title())

#You can also store dicts in dict

users = {
    'aeinstein': {
    'first': 'albert',
    'last': 'einstein',
    'location': 'princeton',
    },
    'mcurie': {
    'first': 'marie',
    'last': 'curie',
    'location': 'paris',
    },
}

for user_name, user_info in users.items():
    print('\nUser name: '+user_name)
    full_name = user_info['first']+' '+user_info['last']
    location = user_info['location']

    print(full_name.title()+' lives in '+location.title())