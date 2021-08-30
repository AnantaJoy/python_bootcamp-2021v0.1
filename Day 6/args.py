def greetings(value = "User"):
    print("Test")
    return "Hello" + value
    
    
print(greetings("Python"))

def add(x,y):
    return x + y

z = add(10,20) + 20
print(z)

# Arbitrary arguments(*args)

def mul(*num):
    z = 1
    for i in num:
        z *= i 
    return z

print(mul(2,3,4,5,6,7))


# keyword arguments
# keywords arbitrary arguments
