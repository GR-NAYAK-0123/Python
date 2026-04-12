
# Inner function - It is a process of defining an another inside one function

def outer_function() :
    print("Now, We are inside outer function :)")

    def inner_function() :                          # The scope of this method is only upto the "outer function"
        print("Now, we are inside Inner function :)") 
    
    inner_function()

    return inner_function      # Here outer_function returning a function (inner_function)
    

#outer_function()      # This method calling

#inner_function()    # We can't access inner_function directly from outside

inner = outer_function()   # Here we got access to the inner_function
inner()                    # Calling the inner_function by using another name