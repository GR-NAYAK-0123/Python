
# Here I am going to take list of numbers, then i am going filter some number based upon certain condition
# For this i am gonna use "filter"

nums = [12, 34, 56, 25, 1, 78, 499]

number_greater_than_50 = list(filter(lambda num : num > 50, nums))

print(number_greater_than_50)