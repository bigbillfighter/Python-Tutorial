class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.miles = 0

    def get_descriptive_name(self):
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()

    def read_miles(self):
        print("This car has "+ str(self.miles)+ " miles on it.")

    def update_miles(self, miles):
        if miles<self.miles:
            print("Can't update the mile be less")
        else:
            self.miles = miles

    def incre_miles(self, miles):
        if miles>0:
            self.miles+=miles

    def fill_gas_tank(self):
        print("Please fill the gas tank!")

class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+"-kWh battary.")

    def get_range(self):
        msg = "This car can go approximately "+str(self.battery_size*3)
        msg +=" miles on a full charge"
        print(msg)

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        print("The car has a "+str(self.battery_size)+"-kWh battary.")

    def fill_gas_tank(self):
        print("This is no gas tank!")