

nums = [2, 4, 7, 12, 11, 34, 9]

firstMax = nums[0]
secondMax = nums[0]

for i in range(len(nums)):
    if nums[i] > firstMax:
        secondMax = firstMax
        firstMax = nums[i]
    elif nums[i] > secondMax:
        secondMax = nums[i]


print(f"The largest element in the list is {firstMax} and second largest is {secondMax}")