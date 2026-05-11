
def longest_substring_without_duplicate(s):
    max_len = 0
    left, right = 0, 0
    result = ''
    d = {}
    n = len(s)
    while right < n:
        if s[right] in d:
            if d[s[right]] >= left:
                left = d[s[right]] + 1
        d[s[right]] = right
        max_len = max(max_len, right-left+1)
        result = s[left:right+1:]
        right += 1
    print(result)
    return max_len


s = 'pwwkew'
print(longest_substring_without_duplicate(s))