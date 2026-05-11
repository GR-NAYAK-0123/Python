
# Two sum problem

def two_sum(nums, target):
    d = {}
    result = [-1, -1]
    for i in range(len(nums)):
        if (target - nums[i]) in d:
            result = [d[target - nums[i]], i]
        else:
            d[nums[i]] = i
    return result

nums = [1, 5, 7, 3, 9]
target = 12

print(two_sum(nums, target))
