mylist = ['January','February','March','April','May','June',12, True] 

print(type(mylist))
print(len(mylist))

# Access
print(mylist[0])
print(mylist[5])
print(mylist[-1])
print(mylist[1:4])

# Append
mylist.append('July')
print(mylist)

# insert
mylist.insert(1, "Insert")  
print(mylist)

# pop
print(mylist.pop(2))
print(mylist)

print(dir(mylist))

mylist.reverse()
print(mylist)
