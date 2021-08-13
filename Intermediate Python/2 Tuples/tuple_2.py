# slicing
a = (1,2,3,4,5,6,7,8)

b = a[2:5]
print(b)  
b = a[::-1]
print(b)

# packing and unpacking

stdnt_info = ("Joy",'EEE',21,'RU')
stdnt_name, dept, age, university = stdnt_info

print(stdnt_name)
print(dept)
print(age)
print(university)

my_tuple = (1,3,5,7,9)
one,two,three,*four = my_tuple
print(one)
print(two)
print(three)
print(four)

# size of tuple and lists
import sys
my_tuple = (1,2,3,True,'Hello')
my_list = [1,2,3,True,'Hello']
print(sys.getsizeof(my_tuple),"bytes")
print(sys.getsizeof(my_list),"bytes")

# timing in tuple and lists

import timeit

print(timeit.timeit(stmt = "(0,1,2,3,4,5)",number=10000000))
print(timeit.timeit(stmt = "[0,1,2,3,4,5]",number=10000000))