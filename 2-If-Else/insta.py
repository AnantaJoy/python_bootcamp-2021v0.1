username = "aquaman101"
password = "finn"

user_name = input("Enter your username: ")
user_password = input("Enter your password: ")

if user_name == username and password == user_password:
    print("Log in Successfully")
    
elif username != user_name:
    print("Wrong Username")

elif password != user_password:
    print("Wrong Password")
    
else:
    print("Log in Failed")