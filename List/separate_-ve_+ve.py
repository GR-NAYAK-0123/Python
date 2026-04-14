

# Here I will define a list and then i will separate all +ve and -ve element from the list

nums = [1, 6, -2, -6, 9, 5, -9]

print("All positive values")

for i in nums:
    if i >= 0:
        print(i)

print("All negative values")

for i in nums:
    if i < 0:
        print(i)

