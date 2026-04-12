
# Here I am going to use "filter" function, which is an inbuild function
# For this method we have to pass one function and one iterable as an argument

nums = [1, 4, 7, 9, 2, 12, 5]

# This is the function that i have passed
# def check_odd(num) :
#     return num % 2 != 0

# Instead of passing this type of method, we can simply pass a lambda function

# check_odd = lambda num : num % 2 != 0

# Instead of this also we can write the lambda function inside the filter

odds = list(filter(lambda num : num % 2 != 0, nums))

print(odds)