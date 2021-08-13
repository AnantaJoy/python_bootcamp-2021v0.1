cardnumber = 101
cardpassword = 111
balance = 10000
inputnumber = int(input("Enter your card number:"))
inputpassword = int(input("Enter your card password"))

if cardnumber == inputnumber:
    if cardpassword == inputpassword:
        money = int(input("Amount of money:"))
        if money <= 10000:
            print("Take your money")
        else:
            print("You don't have enough money.")
    else:
        print("Password does not match")

else:
    print("Card number does not match")