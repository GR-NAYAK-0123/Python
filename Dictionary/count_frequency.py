

nums = [1, 2, 5, 7, 1, 8, 4, 8, 3, 9, 3, 7]

d = {}

for i in nums:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1


print(d)