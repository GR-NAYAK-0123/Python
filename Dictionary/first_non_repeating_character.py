
def first_non_repeating_character(s):
    d = {}

    # This is for counting the frequency
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    # And this one for finding the first non-repeating one
    for i in s:
        if d[i] == 1:
            print(d)
            return i
        

# s = "programming"
s = "Radha"

print(first_non_repeating_character(s))

