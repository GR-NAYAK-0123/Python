
# Check the palindrome

def is_palindrome(s):
    s1 = ""
    s2 = ""
    for i in s:
        if i.isalpha():
            s1 += i.lower()
            s2 = i.lower() + s2
    return s1 == s2


s = "M ada mn "
print(is_palindrome(s))