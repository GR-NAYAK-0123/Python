
# Here I am going do some operation on the list of numbers and i will return only one value
# For this I am gonna use "reduce"

from functools import reduce

nums = [1, 2, 4, 6, 8, 9]

sum_of_nums = reduce(lambda num1, num2 : num1 + num2, nums)

print("Sum of the list : ", sum_of_nums)