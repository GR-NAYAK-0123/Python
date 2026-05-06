
def is_palindrome(s):
    s1 = ""
    s2 = ""
    for i in s:
        if i.isalpha():
            s1 = s1 + i
            s2 = i + s2
    return s1 == s2

s = "m15a7@m778k"
print(is_palindrome(s))