
# Here I am going to do some changing with the list of numbers
# For this I am gonna use "map"

nums = [2, 4, 6, 8, 1, 9]

double_nums = list(map(lambda num : num * 2, nums))

print(double_nums)