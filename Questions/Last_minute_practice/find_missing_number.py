
# Find missing number

def find_missing(nums):
    sum = 0
    for i in nums:
        sum += i
    
    actual_sum = int((nums[-1] * (nums[-1] + 1)) / 2)
    
    return actual_sum - sum

nums = [1, 3, 2, 4, 5, 6, 8]

print(find_missing(nums))