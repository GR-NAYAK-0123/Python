

def element_appeared_twice(nums):
    d = {}
    for i in nums:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    # Finding the element who appeared twice
    result = []
    for i in d:
        if d[i] == 2:
            result.append(i)

    return result


arr = [4, 5, 6, 7, 4, 5, 8]

print("The element who appeared twice are :", element_appeared_twice(arr))