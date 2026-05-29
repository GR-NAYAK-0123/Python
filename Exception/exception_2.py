
# Used the concept Exception handling


try:
    number = int(input("Enter the number? "))
except Exception:
    print("You have typed something other than Integer value")
else:
    print(f"The number is {number}")

