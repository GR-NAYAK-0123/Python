
# Here I am going to write something which will calculate the sum of n natural numbers
# Means sum of the element from 0 to till that number
# For this I am gonna use "for" loop

def sum_n_natural_number(number) :
    sum = 0
    for i in range(number + 1) :
        sum += i
    
    return sum

number = int(input("Enter the number : "))

print("The sum of the",number,"natural number : ", sum_n_natural_number(number))
