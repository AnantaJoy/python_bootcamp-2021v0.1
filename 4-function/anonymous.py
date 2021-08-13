



# def sqr(x):
#     j = []
#     for i in x:
#         j.append(i*i)
#     return j 
      
# y = [1,2,3,4,5]
# z = list(map(lambda k: k*k, y))
# print(z) 

# x = [1,2,3,4,5]
# # print(z(x)) 
# print(sqr(x))


def facto(n):
    if (n == 1 or n == 0):
        return 1
    else:
        return (n * facto(n-1))
n = 8
print(facto(n))