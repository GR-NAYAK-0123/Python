
def decorator(func):
    def wrap(a, b):
        print("Before the addition")
        func(a, b)
        print("After the addition")
    return wrap


@decorator
def addition(a, b):
    print(f"The sum is : {a + b}")


addition(3, 5)

# addition = decorator(addition)     # Instead of using @decorator above the addition method, we can use this
# addition(3, 6)