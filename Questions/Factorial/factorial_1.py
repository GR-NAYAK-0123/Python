
# Here I am going to write a function which will take a number as an argument and it will return factorial value of that number
# Factorial value means product of 1 to n

factorial = 1

def calculate_factorial(number) :
    i = 1
    while i <= number :
        globals()['factorial'] *= i
        i += 1
    return globals()['factorial']

print("The factorial of number 5 : ", calculate_factorial(5))
    
