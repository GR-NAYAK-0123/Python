
# Here I am going to write one lambda function, which will check the number is even or odd
# For this I am gonna use "lambda" keyword

checkEvenOrOdd = lambda num : "Even" if num % 2 == 0 else "Odd"

num = int(input("Enter a number : "))
print(checkEvenOrOdd(num))