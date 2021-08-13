# Ordered, mutable, duplicate elements
my_fruits = ['banana','cherry','apple','orange']
print(my_fruits)

# list constructor
my_list = list(('1', True, 'A'))
my_list1 = list(['A','B', 'C','D'])
# indexing, negative indexing
print(my_fruits[1])
print(my_fruits[-1])

# loop through a lists

for i in my_fruits:
    print(i)
    
# check a element in a lists
if "apple" in my_fruits:
    print("Yes Found")
else:
    print('Not Found')  

#  length of a lists
print(len(my_fruits))

# append a lists
my_fruits.append("blackberry")
print(my_fruits)

# insert a element in a list
my_fruits.insert(3,"grape")
print((my_fruits))

# remove the last element using pop method
my_fruits.pop()
print(my_fruits)

# remove a particular element
my_fruits.remove("apple")
print(my_fruits)

# clear a list
my_fruits.clear()
print(my_fruits)

# sort a list
my_num = [5,-7,1,6,3,9,2]
my_num.sort()
print(my_num)
# crete a list using list comprehension
