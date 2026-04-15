
"""In python dictionary stores the element in key-value pairs format, it's semi-mutable, means we can modify the value but we can't 
   change it's key, It maintains the insertion order but we can acess the value by using the key only, It also a=allows to store
   duplicate values and also all heterogeneous data type
"""

d1 = {1:10, 2:20, 3:30, 4:4}
d2 = {4:40, 5:50, 6:60}

# Here i need to merge two dictionary into one

for i in d2:
    if i in d1:
        d1[i] = d2[i]
    else:
        d1[i] = d2[i]


print(d1)