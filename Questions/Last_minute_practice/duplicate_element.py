
# Duplicate element

def duplicates(nums):
    d = {}
    result = []
    for i in nums:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    for i in d:
        if d[i] > 1:
            result.append(i)
    
    return result

nums = [1, 2, 1, 4, 5, 3, 6, 3, 6, 3]
print(duplicates(nums))
