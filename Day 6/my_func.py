# function define
def myFunc():
    print("Hello, world!")
    
# function call
type(myFunc())

num1 = 100
num2 = 200
num3 = 300
num4 = 400

print(num1 + num2)
print(num3 + num4)

# sum function

def sum(num1, num2):
    return num1 + num2

print(sum(10,20))

# user input 

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

z = sum(x,y)
print(z)

# user info

def userInfo(guestname):
    print("Hello, " + guestname + "! "+"How are "+ guestname)


mylist = ["Rasel","Zihad","Sumaiya","Asraf"]

for i in mylist:
    userInfo(i)