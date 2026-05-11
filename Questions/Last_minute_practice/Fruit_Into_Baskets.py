

def fruit_into_basket(nums):
    d = {}
    left, right = 0, 0
    max_len = 0
    n = len(nums)
    while right < n:
        d[nums[right]] = d.get(nums[right], 0) + 1

        if len(d) > 2:
            d[nums[left]] -= 1
            if d[nums[left]] == 0:
                d.pop(nums[left])
            left += 1
        max_len = max(max_len, right-left+1)
        right += 1
    return max_len


fruits = [1,2,3,2,2]
print(fruit_into_basket(fruits))