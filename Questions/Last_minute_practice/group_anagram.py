
# Group Anagram

def group_anagram(words):
    d = {}
    for i in words:
        s = ''.join(sorted(i))
        if s in d:
            d[s].append(i)
        else:
            d[s] = [i]
    return [x for x in d.values()]

words = ["rat", "tar", "art", "man", "nam", "raja", "ajar", "anm"]
print(group_anagram(words))