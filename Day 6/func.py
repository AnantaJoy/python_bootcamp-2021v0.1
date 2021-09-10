def say_hbd(name):
    print(f"Hello {name}, Happy Birthday.")
    

input = input("Enter your name:")

say_hbd(input)

# Return and None
def say_hbd(name):
    return f"Hello {name}, Happy Birthday."
    

input = input("Enter your name:")

print(say_hbd(input))


# Fizz Buzz Problem