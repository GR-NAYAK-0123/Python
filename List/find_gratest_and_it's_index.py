
nums = [9, 4, 12, 90, 56, 34, 100]

maxValue = -10
index = -1

for i in range(len(nums)):
    if nums[i] > maxValue:
        maxValue = nums[i]
        index = i

print(f"The maximum value is {maxValue} and it's index is {index}")