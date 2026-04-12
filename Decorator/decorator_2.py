
def logger(fun):
    def wrap():
        print("Before method calling :)")
        fun()
        print("After method calling :)")

    return wrap

@logger
def greet():
    print("Hello Python")

# Instead of above annotation we can write -> greet = logger(greet)
greet()

