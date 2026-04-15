
def twoSum(nums, target):
    d = {}
    for i in range(len(nums)):
        if target-nums[i] in d:
            return [i, d[target-nums[i]]]
        d[nums[i]] = i
    return [-1, -1]


nums = [2, 7, 11, 15]
target = 26

print(twoSum(nums, target))