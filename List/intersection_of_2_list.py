
# Here I have to check the intersection of 2 list and i have to print those

def intersection(l1, l2):
    d = {}
    for i in l1:
        if i in d:
            continue
        d[i] = 1
    ans = []
    for i in l2:
        if i in d and d[i] == 1:
            ans.append(i)
            d[i] = 0
    return ans
        
l1 = [1, 2, 3, 4]
l2 = [2, 2]

print(intersection(l1, l2))