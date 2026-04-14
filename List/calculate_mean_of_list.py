
# Here i am gonna calculate the mean of the list
# Here mean is the sum of the element in the list divided by the length of the list

nums = [4, 5, 9, 2, 1]

sum = 0
length = len(nums)

for i in nums:
    sum += i

print("The mean of this list is :",sum/length)