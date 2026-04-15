
# Here I am gonna write the program to sum all the values present in the dictionary

d = {1:10, 2:20, 5:50, 7:70}

sum = 0

for i in d:
    sum += d[i]

print(f"The sum is {sum}")