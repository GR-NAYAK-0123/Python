
def getting_deco(fun):
    def wrap(a, b):
        if a < b:
            a,b = b,a
        result = fun(a, b)
        return result
    return wrap

@getting_deco
def sub(a, b):
    return a - b

# sub = getting_deco(sub)

result1 = sub(2, 4)
print(result1)