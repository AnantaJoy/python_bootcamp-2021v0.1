# ordered, immutable, duplicate elements
my_tuple = ('Ananta',21,'Bangladesh')
my_tuple2 = "Joy", 22, "Germany"
my_tuple3 = ('Asim',)
my_tuple4 = tuple((my_tuple2))

print(my_tuple4)

# access an element/elements 
std_name = ('Joy','Johny','John','Elton')
std_name1 = std_name[1:4]
print(std_name1) 

# iterate over a tuple
for i in std_name:
    print(i)
    
# check condition
if "Joy" in std_name:
    print("Yes")
else:
    print("No")
    
# count method in tuple
number_list = (1,3,2,3,4,5,6,6,7)

print(number_list.count(3))

# tuple to list to tuple

my_tuple = ('X','Y','Z')

my_list = list(my_tuple)
print(my_list)

my_tuple2 = tuple(my_list)
print(my_tuple2)