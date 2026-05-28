
# Here I am going write some method and those method does not have any name
# For this I am gonna use "lambda" keyword

function = lambda num1 : num1 * num1

num1 = int(input("Enter a number : "))
result = function(num1)
print(result)


s = "Radha"
print(s.sort())
print(sorted(s))