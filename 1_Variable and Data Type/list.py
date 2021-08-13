# list
fruits_list = ['banana', 'apple', 'orange', 'watermelon', 'cherry']
print(fruits_list)

months_list = ['January', 'February', 'March', 'April',
               'May', 'June', 'July', 'August', 'September', 'October',
               'November','January']
# print the list of months
print(months_list)

# slicing the list
print(months_list[1:4])
print(months_list[-2])

# length of the list
print(len(months_list))

# Add a new month 'December'
months_list.append('December')
print(months_list)

# reverse a list of months
months_list.reverse()
print(months_list)

# Count a item in the list
print(months_list.count('January'))

# sorting
months_list.sort()
print(months_list)
# copy a list of months
months_list2 = months_list.copy() 


