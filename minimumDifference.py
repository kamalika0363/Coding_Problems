"""
Function Description
Complete the function getMinimumDifference in the editor below.

getMinimumDifference has the following parameter(s):
    string a[n]: an array of strings
    string b[n]: an array of strings

Return int[n]: the minimum number of characters in either string that needs to be modified to make the two strings
anagrams or -1 if it is not possible

Constraints
• Each string consists of lowercase characters [a-z]
• 1 ≤ n ≤ 100
• 0 ≤ |a[i]|, |b[i]| ≤ 10⁴
• 1 ≤ |a[i]| + |b[i]| ≤ 10⁴
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
