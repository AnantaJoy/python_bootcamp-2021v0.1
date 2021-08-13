def my_fact(n):
    
    if n == 0 or n == 1:
        return 1
    else:
        return n * my_fact(n-1)
    

z = my_fact(6)
print(z)

def my_fact(n):
    if n == 0 or n==1:
        return 1
    else:
        j = 1
        while n > 1:
            j = n*j
            n = n-1
        return j
  
print(my_fact(6))          
    
    
    
 