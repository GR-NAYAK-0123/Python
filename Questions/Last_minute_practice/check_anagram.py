
# Check Anagram

def check_anagram(s1, s2):
    d = {}
    for i in s1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in s2:
        if i in d:
            d[i] -= 1
        else:
            d[i] = 1
    for i in d:
        if d[i] != 0:
            return False
        
    return True

s1 = "Raja"
s2 = "ajRa"

print(check_anagram(s1, s2))