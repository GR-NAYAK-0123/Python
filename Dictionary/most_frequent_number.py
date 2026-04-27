
# Finding the most frequent element

def most_frequent(nums):
    d = {}
    for i in nums:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    # Traversing the dictionary for finding the most frequent element
    most_freq = nums[0]
    for i in d:
        if d[i] > d[most_freq]:
            most_freq = i

    print(d)
    
    return most_freq


arr = [1,2,3,1,2,1,4,5,2]

print("Most frequent element is :", most_frequent(arr))