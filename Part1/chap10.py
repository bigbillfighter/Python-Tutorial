#process files
#read files
#here use open() to return an object that represents a file
#use with we can guarantee that the file will be closed after the with-block
#if we use close() to close the file ,sometimes the file may be closed wrongly or
#just didn't get closed
with open('txt/txt_chap10.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
#use read will result in the fact that there will be an empty line
#in the end of the file
#Because read() will return an empty string when reading to the end of the file
#and an empty sting will be displayed as an empty line

#read every line
#the code means after reading a file-path, the file object is a list with elements which is a line in the file
file_path = 'txt/txt_chap10.txt'
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())

#if not use .rstrip(), there will be one line after every ouput line, because
#read() set one empty string after every line
with open(file_path) as file_object:
    for line in file_object:
        print(line)

#the file_object will be deleted when with-block ends
#We can store the contents in a list with readlines() method
with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

pi_string = ''
for line in lines:
    pi_string+=line.strip()
print(pi_string)
print(len(pi_string))

#we can use float() to transfer the string to a float number forcely
pi_val = float(pi_string)
print(pi_val)

file_path = 'txt/pi_million_digits.txt'
pi_string = ''
with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    pi_string+=line.strip()
print(pi_string[:52]+'...')
print(len(pi_string))
birthday = '1017'
if birthday in pi_string:
    print('yes')
else:
    print('no')

#we can use replace() to replace one string to another when appearing in a long string
msg = 'I really like dogs'
print(msg.replace('dog', 'cat'))
#the influence of .replace() is temperary not permanent
print(msg)

file_path = 'txt/programming.txt'
sm = ''
lsm = ''
with open(file_path) as file_object:
    sim_str = file_object.readlines()
for line in sim_str:
    sm = line.replace('love', 'like').strip()
    lsm+=line.strip()
    print(sm)

print(lsm)


