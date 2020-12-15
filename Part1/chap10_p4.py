#json files
#use json.dump to write and json.load to read

import json
numbers = [2, 3, 5, 7, 11, 13]
filename = 'json/numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

with open(filename) as f_obj:
    new_num = json.load(f_obj)

print(new_num)

filepath = "json/username.json"
try:
    with open(filepath) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    with open(filepath, 'w') as f_obj:
        username = input("What is your name?")
        json.dump(username, f_obj)
        print("We'll remember you when you come back, "+username+" !")
else:
    print("Welcome back, "+username+" !")



