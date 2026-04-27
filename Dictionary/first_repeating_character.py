

def first_repeating(s):
    d = {}
    for i in s:
        if i in d:
            return i
        else:
            d[i] = 1
    
    print(d)


# s = "swiss"
s = "abcd"

print("First repeating character is :", first_repeating(s))