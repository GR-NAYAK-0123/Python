
def decorator(func):
    def wrap(*args):
        print("Before")
        func(*args)
        print("After")
    return wrap

@decorator
def add(*args):
    sum = 0
    for i in args:
        sum += i
    print(f"The sum is {sum}")


add(1, 4, 7, 2, 9, 0, 77)