
# Here I am going to print all the number from 0 to 10 and I will skip those numbers which is divisible by 4
# For this operation I am going to use "continue" keyword
# And for printing the number I will use "for" loop

for value in range(11) :
    if value % 4 == 0 :
        continue

    print(value)

print("Operation Done :)")

