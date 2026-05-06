
# Top k frequent element in a list

def top_k_frequent(nums, k):
    d = {}
    for i in nums:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    values = [x for x in d.items()]
    values.sort(key=lambda x:x[1], reverse=True)
    return [values[x][0] for x in range(k)]

nums = [1, 2, 2, 3, 2, 3, 2, 3, 2, 1, 1, 1, 4]
k = 3
print(top_k_frequent(nums, k))