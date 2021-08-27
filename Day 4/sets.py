# sets

set1 = {1,2,3,4,4,5,5,6,6,7,7,'string'}

# no duplicate value
print(set1)

print(len(set1))
print(type(set1))

set1 = {1,3,5,7} 
set2 = {2,4,5,6,}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2)) 

print(dir(set1))