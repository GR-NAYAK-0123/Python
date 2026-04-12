
# Here I am going to write one line expression which calculate sum of cube of all the numbers from the list
# For this I am gonna use "reduce" and "map"

from functools import reduce

nums = [2, 3, 4]

print(reduce(lambda num1, num2 : num1 + num2, list(map(lambda num1 : num1 * num1 * num1, nums))))