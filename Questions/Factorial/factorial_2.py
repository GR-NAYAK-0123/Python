
# Here I am going to calculate the factorial of a number by using "for" loop

def calculate_factorial(number) :

    factorial = 1

    for i in range(1, number + 1) :
        factorial *= i
    
    return factorial

print("Factorial of 6 : ", calculate_factorial(6))