#class
from class_chap9 import *

class Dog():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title()+" is now sitting.")

    def roll_over(self):
        print(self.name.title()+" rolled over!")

    def print_sen(self):
        print("ok")


my_dog = Dog('wiLLim', 6)
print("My dog's name is "+my_dog.name.title()+" .")
#_init_() metheod will return an object although not exists 'return' clearly
my_dog.sit()
my_dog.roll_over()
my_dog.print_sen()
#self must be included in all of the methods of a class
print()


my_car = Car('audi', 'a4', 2016)
print(my_car.get_descriptive_name())
my_car.read_miles()
my_car.miles = 10
my_car.read_miles()
my_car.update_miles(20)
my_car.read_miles()


my_electriccar = ElectricCar('tesla', 'model s', 2016)
print('\n'+ my_electriccar.get_descriptive_name())
my_electriccar.fill_gas_tank()
my_car.fill_gas_tank()
my_electriccar.battery.describe_battery()
my_electriccar.battery.get_range()