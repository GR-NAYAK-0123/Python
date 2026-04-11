
# Higher Order function - It is a process of providing a function as an argument to another function

# This is normal function
def addition(num1, num2) :
    return num1 + num2

# This is another normal function
def substraction(num1, num2) :
    return num2 - num1

# But this is not a normal function, This is a higher order function which takes another function as an argument
def operation(num1, num2, function) :
    return function(num1, num2)

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

# result = operation(num1, num2, addition)
result = operation(num1, num2, substraction)
print(result)

