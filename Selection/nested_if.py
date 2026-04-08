
# Here I will take an input(age) from the user and determine they are eligible for vote or not
# If they are eligible then i will check for senior citizen

age = int(input("Enter your age : "))

if age >= 18 :
    print("Congradulations, You are eligible for vote :) ")
    if age > 50 :
        print("You are comes under the category of senior citizen !!!")
    else :
        print("You are not comes under the category of senior citizen !!!")
else :
    print("You are not eligible for vote ): ")