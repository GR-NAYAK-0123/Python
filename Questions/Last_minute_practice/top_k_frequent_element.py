
# Top k frequent element in a list

def top_k_frequent(nums, k):
    d = {}
    for i in nums:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    values = [i for i in d.items()]
    values.sort(key=lambda x: x[1], reverse=True)
    return [values[i][0] for i in range(k)]

nums = [1, 2, 2, 3, 2, 3, 2, 3, 2, 1, 1, 1, 4]
k = 3
print(top_k_frequent(nums, k))