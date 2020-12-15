import fun_chap8
from fun_chap8 import fun_make_pizza as mp

#function
def greet_user(username):
    """display simple greeting sentences"""
    print('Hello, '+username+' !')

greet_user('Lucas')

def describe_pet(animal_type, pet_name):
    """dispaly the information of pets"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

#transfer the name of key words
describe_pet('hamster', 'harry')
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='ketty', animal_type='cat')

#define function with default value
#coefficients with default values can only be defined in the end
def describe_pet(pet_name, animal_type='dog'):
    """dispaly the information of pets"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('Mike')
describe_pet('Mike', 'cat')
describe_pet(pet_name='Mike')
describe_pet(pet_name='Mike', animal_type='Cat')

def get_format_name(first_name, last_name):
    full_name = first_name+' '+last_name
    return full_name.title()

musician = get_format_name('lucas', 'park')
print('\n'+musician)

#use default values to control coefficent numbers
def get_formatted_name(first_name, last_name, middle_name=''):
    """return name"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print('\n'+musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print('\n'+musician)

def build_person(first_name, last_name):
    person = {'first name': first_name, 'last name': last_name}
    return person

musician = build_person('lucas', 'park')
print()
print(musician)
print()

def greet_user(names):
    for name in names:
        msg = 'Hello, '+name+'!'
        print(msg)

user_name = ['hannah', 'ty', 'margpt']
greet_user(user_name)

def build_person(first_name, last_name):
    person = [first_name,  last_name]
    return person

musician = build_person('lucas', 'park')
print()
print(musician)
print()

def greet_user(names):
    for name in names.values():
        msg = 'Hello, '+name+'!'
        print(msg)

user_name = {'A': 'hannah', 'B': 'ty', 'C': 'margpt'}
greet_user(user_name)

print()
#the changes functions do on list or dictionary is permanent
# 首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# 模拟打印每个设计，直到没有未打印的设计为止
# 打印每个设计后，都将其移到列表completed_models中
while unprinted_designs:
    current_design = unprinted_designs.pop()
    #模拟根据设计制作3D打印模型的过程
    print("Printing model: " + current_design)
    completed_models.append(current_design)
# 显示打印好的所有模型
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)


def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # 模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

print()
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print()
print(unprinted_designs)

#we can use the slice to transfer the copied version to the function
#Thus the raw data won't be influenced
print()
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print()
print(unprinted_designs)

#use tuple to store infinite position paramaters
def make_pizza(size, *topppings):
    print("\nMaking a "+str(size)+" inch pizza with following toppings:")
    for toppping in topppings:
        print("- "+toppping)

make_pizza(16 ,'tomato')
make_pizza(22,'potato', 'mushroom', 'cucumber')

#use dicitonary to store infinite key word paramaters
def build_profile(first, last, **info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in info.items():
        profile[key] = value
    return profile

user_info = build_profile('lucas', 'park', age=12, weight = 65)
print()
print(user_info)

def build_person(first, last, *ok,  **info):
    person = {}
    person['first_name'] = first
    person['last_name'] = last
    shoes = {}
    i=0
    for shoe in ok:
       shoes[str(i)] = shoe
       i+=1
    person['shoes'] = shoes
    for key, value in info.items():
        person[key] = value

    return person

oneself = build_person('lucas', 'park', 'LiNing', 'Adidas', 'Nike', age=12, weight = 65)
print()
print(oneself)

#the tuple and dictionary that make infinate parameters can be used simultaneaously

#import function module to use the function.
#Actually, python interpreter just copy the codes from python files we imported here
#and execute them
fun_chap8.fun_make_pizza(16, 'tomato', 'fish', 'bacon')
#use alias to call the funciton
mp(12, 'chili')

#"from mudule_name import * " means you can directly use all the functions
#the module has with their own names instead of alias or module_name.function_name
#so this method is very dangerous when you use big package libraries that aren't written by yourself

#The safer method is that only import the functions you would like to use with clear names
#or just use the form like module_name.function_name

'''
There are some tips about defining funcitons.
1.Don't use blanks to split key conefficients with defualt values.
  So as use key coefficients to call functions
2.Don't write code with any line more than 79 letters including blanks.
  And don't let annotation with any line more than 72 letters including blanks
3.Define funciton with 2 Tabs when the parameter list is longer than one line,
  like:
    def function_name(
            parameter_0, parameter_1, parameter_2
            parameter_3, parameter_4):
        function_body...
'''




