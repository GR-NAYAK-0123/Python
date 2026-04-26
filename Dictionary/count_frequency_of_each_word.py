
def count_frequency_of_word(s):
    # This split() will separate those words
    words = s.split()

    d = {}

    for i in words:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    return d


# sentence = "hello world hello python world"
sentence = "Radha Radha Radha Radha"

print(count_frequency_of_word(sentence))
