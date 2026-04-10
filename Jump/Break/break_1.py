
# Here I am going to print some number from 0 to 10 but when the number will reached to 5 then, I will stop printing
# For this I will use "break" keyword
# "break" keyword means, Whenever interpreter came across "break" statement then it will came out from the loop

for value in range(10) :
    if value == 5 :
        break

    print(value)

print("Operation Over")