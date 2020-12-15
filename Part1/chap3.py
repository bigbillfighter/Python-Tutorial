#list
#output list
stuffs = ['motorcycle', 'triangle','cirlce', 'microwave oven']
print(stuffs)
print(stuffs[-1].title())#visit the last element
stuffs.append('Gucci')
print(stuffs)

elmt=[]
elmt.append('ok')
elmt.append('all right')
elmt.append('sorry')
print(elmt)
elmt.insert(2,'Hello')
print(elmt)

del elmt[0]#delete element
print(elmt)
elmt_end = elmt.pop()#pop the end and return value
print(elmt)
print(elmt_end)
elmt.append('sudoko')
elmt.pop(1)
print(elmt)

elmt.insert(1,'honor')
result = 'expensive'
elmt.append('he')
elmt.append('she')
elmt.append((result))
print(elmt)

#delete element by the name
elmt.remove('he')
print(elmt)

#sort the list. sort() can change the list permanently
print(elmt.sort())
print(elmt)
#sort the list be reversed
print(elmt.sort(reverse=True))
print(elmt)

#use sorted() to sort the list temporary
print(sorted(elmt))
print(elmt)
#sorted() can also sorted reversed
elmt.sort()
print(elmt)
print(sorted(elmt,reverse=True))
print(elmt)

#reverse() can change the order permanently
stf = ['all right', 'expensive', 'honor', 'she', 'sudoko']
print(stf.reverse())
print(stf)

#use len() to calculate the len of list
print(len(stf))