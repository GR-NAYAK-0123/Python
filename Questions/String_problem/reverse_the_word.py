
# Reversing the words from a sentence

def reverse_words(sentence):
    words = sentence.split()
    words.reverse()
    return ' '.join(words)


sentence =  "I love Python"

print(reverse_words(sentence))