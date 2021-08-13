# create a list using loop
my_list = []
for i in range(1,10):
    my_list.append(i)
    
print(my_list)

# print a particular range
print(my_list[1:5])

# coping a list
list1 = [1,2,3]
list2 = list1.copy()

list2.append(3)
print(list1)
print(list2)

# list comprehension

list3 = [1,2,3,4,5]
sqr_list = [i*i for i in list3]
print(list3)
print(sqr_list)
