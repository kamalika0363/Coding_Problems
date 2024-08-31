"""
An anagram is a word whose characters can be rearranged to create another word. Given two strings, determine the
minimum number of characters in either string that must be modified to make the two strings anagrams. If it is not
possible to make the two strings anagrams, return -1.

Example:
a = ['tea', 'tea', 'act']
b = ['ate', 'toe', 'acts']

• a[0] = tea and b[0] = ate are anagrams, so 0 characters need to be modified

• a[1] = tea and b[1] = toe are not anagrams. Modify 1 character in either string to make them anagrams.

• a[2] = act and b[2] = acts are not anagrams and cannot be converted to anagrams because they contain different
numbers of characters.

The return array is [0, 1, -1]
"""


def min_chars_to_anagram(a, b):
    if len(a) != len(b):
        return -1

    a_count = {}
    b_count = {}

    for char in a:
        if char in a_count:
            a_count[char] += 1
        else:
            a_count[char] = 1

    for char in b:
        if char in b_count:
            b_count[char] += 1
        else:
            b_count[char] = 1

    diff_count = 0
    for char in a_count:
        if char not in b_count:
            diff_count += a_count[char]
        else:
            diff_count += abs(a_count[char] - b_count[char])

    return diff_count


def min_chars_to_anagram_list(a, b):
    result = []
    for i in range(len(a)):
        result.append(min_chars_to_anagram(a[i], b[i]))
    return result


# Driver function
def driver():
    a = ['tea', 'tea', 'act']
    b = ['ate', 'toe', 'acts']
    print(min_chars_to_anagram_list(a, b))  # Output: [0, 1, -1]


# Test cases
def test():
    print(min_chars_to_anagram('tea', 'ate'))  # Output: 0
    print(min_chars_to_anagram('tea', 'toe'))  # Output: 1
    print(min_chars_to_anagram('act', 'acts'))  # Output: -1
    print(min_chars_to_anagram('hello', 'world'))  # Output: 4


driver()
test()
