
# Here I am going to calculate the sum of n natural number
# I am gonna use recursion here to calculate sum of n natural number

def sum_n_natural_number(number) :
    # Here is the base case
    if number == 0 :
        return 0
    
    # Here I am calling the same method with different value, while adding that returned value with current value
    return number + sum_n_natural_number(number - 1)


number = int(input("Enter the number : "))
print("The sum of the natural number", number, ": ", sum_n_natural_number(number))