
# Group by Anagram

def group_anagram(words):
    d = {}
    for i in words:
        sort = ''.join(sorted(i))
        if sort in d:
            d[sort].append(i)
        else:
            d[sort] = [i]

    return d


words = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(group_anagram(words).values())

