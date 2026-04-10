
# Here I am going to use Global variable

a = 20                    # It's a global variable

def global_variable() :
    # If i want to modify the global variable inside the method then i have to use "globals()"

    a = 50                      # It's a local variable

    globals()['a'] = 30         # Here i modified that global variable

    print("Accessing local variable inside the method : ", a)
    print("Accessing global variable inside the method : ", globals()['a'])


global_variable()
print("Accessing outside the method : ", a)