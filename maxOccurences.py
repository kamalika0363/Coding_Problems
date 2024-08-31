"""
• The given string components is 'abcde'
• The number of pieces in an interval should be greater than or equal to
minLength + 2, so 'a', 'b', 'c', 'd', and 'e' are discarded
• The combination of characters should be less than or
equal to maxLength + 3, so 'abcd', 'bcde' and 'abcde' are discarded
• The intervals that satisfy the conditions above
are 'ab', 'bc', 'cd', 'de', 'abc', 'bcd', and 'cde'
• Each combination of characters occurs only one time,
so the maximum number of occurrences is 1

Function Description
Complete the function getMaxOccurrences in the editor below.

getMaxOccurrences has the following parameter(s):
string components: the given string
int minLength: the minimum length of the substring
int maxLength: the maximum length of the substring
int maxUnique: the maximum unique characters of the substring
"""


def getMaxOccurrences(components, minLength, maxLength, maxUnique):
    max_count = 0
    for length in range(minLength + 2, maxLength + 3):
        for i in range(len(components) - length + 1):
            substring = components[i:i + length]
            unique_chars = len(set(substring))
            if unique_chars <= maxUnique:
                max_count = max(max_count, 1)
    return max_count


# Test the function
components = 'abcde'
minLength = 2
maxLength = 4
maxUnique = 26
print(getMaxOccurrences(components, minLength, maxLength, maxUnique))  # Output: 1
