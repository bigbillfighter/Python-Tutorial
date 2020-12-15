#error process
from fun_chap10 import count_words

##print(5/0)
#if we run the code above, there will be a traceback printed on the console
#This will trigger an error called ZeroDivisionError
#It is an error object
#we can use try-except block to catch the error
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divided by zero!")

#use else to execute other actions if not triggered error

##print("\nInput two numbers to do a division.")
##print("Enter 'q' to quit.")

##while True:
    ##first_num = input("\nInput the first number:")
    ##if first_num=='q':
        ##break
    ##second_num = input("Second number:")
    ##if second_num == 'q':
        ##break
    ##try:
        ##answer = int(first_num)/int(second_num)
    ##except ZeroDivisionError:
        ##print("Can't divide by zero!")
    ##else:
        ##print(answer)

file_name = 'txt/alice_story.txt'

try:
    with open(file_name) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = "Sorry, the file "+file_name+" does not exsit."
    print(msg)

#use split to split the string with blank
title = "Alice in Wonderland"
tslice = title.split()
print(tslice)

file_name = 'txt/alice.txt'
count_words(file_name)

filenames = ['txt/alice.txt', 'txt/siddhartha.txt', 'txt/moby_dick.txt', 'txt/little_women.txt']
for filename in filenames:
    count_words(filename)

#use pass to do not do anything
try:
    print(5/0)
except ZeroDivisionError:
    pass

#use TypeError to denote the wrong type the program transfers
a = '10'
b = 3
try:
    print(str(a/b))
except TypeError:
    print("Wrong type!")

#use count() to calculate how many times a string appears in a long string(text)
def count_times(filename, words):
    with open(filename) as f_obj:
        number=f_obj.read().lower().count(words)
        return number

txtname = "txt/little_women.txt"
num = count_times(txtname, "she")
print('\n'+"'she' appears "+str(num)+" times in "+txtname)






