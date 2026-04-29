

nums = [2, 4, 7, 12, 11, 34, 9]

# firstMax = nums[0]
# secondMax = nums[0]

# Efficient approach
# for i in range(len(nums)):
#     if nums[i] > firstMax:
#         secondMax = firstMax
#         firstMax = nums[i]
#     elif nums[i] > secondMax:
#         secondMax = nums[i]

nums.sort()
first_max = nums[-1]
second_max = float('-inf')

# Not very efficient approach
for i in range(len(nums)-1, -1, -1):
    if nums[i] < first_max:
        second_max = nums[i]


print(f"The largest element in the list is {first_max} and second largest is {second_max}")