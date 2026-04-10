
# Here I am going to calculate the factorial of a number by using recursion
# Recursion is basically is a process of calling a method itself on certain base condition

def calculate_factorial(number) :
    # This is the base condition for this recursion
    if number == 1 :
        return 1
    
    return number * calculate_factorial(number - 1)


number = int(input("Enter a number : "))
print("The factorial of ",number," : ", calculate_factorial(number))