
# Frequency of character

def frequency(s):
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

s = "Radha"

print(frequency(s))