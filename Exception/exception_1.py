

print("Application started and Resource opened !!!")


try:
    a = int(input("Enter the numerator : "))
    b = int(input("Enter the denomenator : "))

    print("The result is :", a/b)

except Exception as e:
    print("You have made some mistake", e)
finally:
    print("Resource closed :)")