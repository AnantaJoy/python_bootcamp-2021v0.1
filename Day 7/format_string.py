# # Replacing concatenation
# firstName = f"C:\\root\d\\v"
# print(firstName)

firstName = "John"
secondName = "Doe"
# fullName = firstName + secondName 
fullName = "{1} {0}".format(firstName, secondName)
print(fullName)