# scope

x = "I am Global"

def scope():
    global y
    y = "I am Local"
    # print(x)
    # print(y)

scope()   
print(x)
print(y)