#write files

#use open(, 'w') to write on a file. If not exists, program will
#build it automatically.
#the second coefficient in open() includes 'w', 'r', 'a', 'r+'
#'r' means 'read'; 'w' means 'write'; 'a' means 'add'; 'r+' means 'read and write'
#if not transfer, use 'r' as default
filename = 'txt/chap10.txt'
with open(filename, 'w') as file_object:
    file_object.write("My name is Burry Alen.\n")
    file_object.write("And I am the fastest man in the world!\n")

with open(filename, 'a') as file_object:
    file_object.write("When I was seven years old, my mother was killed by something impossible.\n")
    file_object.write("And my father was thus in poision.")

with open(filename, 'r+') as file_object:
    file_object.write("Hello world!")





