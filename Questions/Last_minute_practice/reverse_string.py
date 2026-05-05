
# Reversing a string

def reverse(s):
    rev = ""
    for i in s:
        rev = i + rev
    return rev

s = "Radha"
print(reverse(s))