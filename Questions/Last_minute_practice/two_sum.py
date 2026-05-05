
# Two sum

def two_sum(nums, target):
    d = {}
    for i in range(len(nums)):
        if (target - nums[i]) in d:
            return [d[target - nums[i]], i]
        else:
            d[nums[i]] = i
    return [-1, -1]

nums = [1, 4, 7, 3, 9]
target = 10

print(two_sum(nums, target))
