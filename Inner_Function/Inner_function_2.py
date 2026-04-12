
#Outer function
def greet() :
    # Inner function
    def message() :
        print("Welcome to Python")
    
    # From outer function we are calling inner function (message)
    message()


# Calling outer function
greet()