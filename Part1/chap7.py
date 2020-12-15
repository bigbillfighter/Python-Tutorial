#Input and while loop
##msg = input("Tell me something:")
##print(msg)

#use int() to transform to number forcely
##age = int(input('How old are you: '))
##if age > 18:
##    print("You are an adult")

#calcualte module
a = 10
if a%2==1:
    print('a is odd')
else:
    print('a is even')

#while loop
a = list(range(1,10))
for s in a:
    print(s)
    if s>6:
        break

print()
i=0
s = a[i]
while True:
    print(s)
    if i>5:
        break
    i+=1
    s = a[i]

c = []
while a:
    p = a.pop()
    if p>5:
        print(p)
    print('......')
    c.append(p)
print(c)
print(a)
#In loop, if the list is empty, the condition can ben seen as False;
#instead, if not empty, seen as True
