

def flatten(nums):
    result = []

    for i in nums:
        if isinstance(i, list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result


nums = [1, [2, [3, 4], 5], [1, 2]]

print(flatten(nums))