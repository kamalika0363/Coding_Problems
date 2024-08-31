"""
For each word in a list of words, if any two adjacent characters are equal, change one of them.
Determine the minimum number of substitutions so the final string contains no adjacent equal characters.
Example
words = ['add', 'boook', 'break']
1. 'add': change one d(1 change)
2. 'boook: change the middle o(1 change)
3. 'break': no changes are necessary (0 changes)

The return array is [1,1,0].
"""


def min_substitutions(words):
    res = []
    for word in words:
        subs = 0
        i = 0
        while i < len(word) - 1:
            if word[i] == word[i + 1]:
                subs += 1
                i += 1
            i += 1
        res.append(subs)
    return res


# Test the function
words = ['add', 'boook', 'break']
print(min_substitutions(words))  # Output: [1, 1, 0]
